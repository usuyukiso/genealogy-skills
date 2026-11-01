// Crop part of a scan at full resolution (for reading handwriting).
// Build once:  swiftc -O crop.swift -o /tmp/scan_crop
// Use:         /tmp/scan_crop <in> <out.jpg> <x0> <x1> <y0> <y1>
//   fractions of width/height, e.g. 0.07 0.93 0 1 = spread without margins,
//   0.15 0.70 0.26 0.46 = one entry zoomed. Reads jpg/png/jxl (macOS ImageIO).
// `sips -c` ignores the offset on some files — use this instead.
import Foundation
import ImageIO
import UniformTypeIdentifiers

let a = CommandLine.arguments
let src = CGImageSourceCreateWithURL(URL(fileURLWithPath: a[1]) as CFURL, nil)!
let img = CGImageSourceCreateImageAtIndex(src, 0, nil)!
let w = Double(img.width), h = Double(img.height)
let x0 = Double(a[3])!, x1 = Double(a[4])!
let y0 = a.count > 5 ? Double(a[5])! : 0, y1 = a.count > 6 ? Double(a[6])! : 1
let r = CGRect(x: w * x0, y: h * y0, width: w * (x1 - x0), height: h * (y1 - y0))
let c = img.cropping(to: r)!
let dst = CGImageDestinationCreateWithURL(URL(fileURLWithPath: a[2]) as CFURL,
                                          UTType.jpeg.identifier as CFString, 1, nil)!
CGImageDestinationAddImage(dst, c, [kCGImageDestinationLossyCompressionQuality: 0.85] as CFDictionary)
CGImageDestinationFinalize(dst)
