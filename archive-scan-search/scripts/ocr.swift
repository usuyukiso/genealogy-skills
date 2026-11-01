import Foundation
import Vision
import ImageIO

// usage: swift ocr.swift <srcRoot> <outDir>
let args = CommandLine.arguments
let src = URL(fileURLWithPath: args[1])
let out = URL(fileURLWithPath: args[2])
try? FileManager.default.createDirectory(at: out, withIntermediateDirectories: true)
let exts: Set<String> = ["jpg", "jpeg", "jxl", "png"]
let en = FileManager.default.enumerator(at: src, includingPropertiesForKeys: nil)!
var files: [URL] = []
for case let u as URL in en where exts.contains(u.pathExtension.lowercased()) {
    if u.path.contains("/_ocr/") { continue }
    files.append(u)
}
files.sort { $0.path < $1.path }
var n = 0
for u in files {
    n += 1
    let folder = u.deletingLastPathComponent().lastPathComponent
    let name = folder + "__" + u.deletingPathExtension().lastPathComponent + ".txt"
    let dst = out.appendingPathComponent(name)
    if FileManager.default.fileExists(atPath: dst.path) { continue }
    guard let isrc = CGImageSourceCreateWithURL(u as CFURL, nil),
          let img = CGImageSourceCreateThumbnailAtIndex(isrc, 0, [
            kCGImageSourceCreateThumbnailFromImageAlways: true,
            kCGImageSourceThumbnailMaxPixelSize: 2000,
            kCGImageSourceCreateThumbnailWithTransform: true] as CFDictionary)
    else { print("FAIL \(u.path)"); continue }
    let req = VNRecognizeTextRequest()
    req.recognitionLanguages = ["ru-RU"]
    req.recognitionLevel = .accurate
    req.usesLanguageCorrection = false
    try? VNImageRequestHandler(cgImage: img).perform([req])
    let text = (req.results ?? []).compactMap { $0.topCandidates(1).first?.string }.joined(separator: "\n")
    try? text.write(to: dst, atomically: true, encoding: .utf8)
    if n % 200 == 0 { print("\(n)/\(files.count)") }
}
print("DONE \(files.count)")
