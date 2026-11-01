"""Raw place index per delo from OCR (Peasant Land Bank style files).

  python3 -I idx.py <_ocr dir> <frames.tsv> > idx.txt

One line per delo: T — names of товарищества/общества («Лазукинское т-во»),
W — «… волости», P — text after «волости, при …», V — «дер. …».
Raw OCR: every name needs checking; it is a lead list, not a result.
"""
import sys,re,os,collections
ocr,tsv=sys.argv[1],sys.argv[2]
fr=[l.rstrip('\n').split('\t') for l in open(tsv,encoding='utf-8')]
L=r'[А-ЯЁа-яёіѣъ\-]'
P=[('T',re.compile(r'([А-ЯЁ]'+L+r'{3,}(?:ск|цк)(?:ому|имъ|имь|им|ое|аго|ого|ій|ий))\s*(?:\d+\s*-?\s*\w*\s*)?(?:\d*\s*дом\w*\.?\s*)?(?:т\s*-\s*в|товарищ|сельск|общ)')),
   ('P',re.compile(r'вол\w*\s*[,.]?\s*((?:при|въ|вь|в)\s.{3,45})')),
   ('V',re.compile(r'(?:\bдер\s*\.|деревн[яиеюь])\s*([А-ЯЁ]'+L+r'{3,}(?:\s*-\s*[А-ЯЁ]'+L+r'+)?)')),
   ('W',re.compile(r'([А-ЯЁ]'+L+r'{3,}(?:ской|скої|ской))\s*(?:вол|вл)'))]
out=collections.OrderedDict()
for a,b,c in fr:
    t=re.sub(r'\s+',' ',open(os.path.join(ocr,f'{a}__{b}.txt'),encoding='utf-8').read())
    for k,p in P:
        for m in p.finditer(t):
            out.setdefault(c,collections.Counter())[(k,m.group(1).strip())]+=1
for c,cnt in out.items():
    parts=[]
    for k in 'TWPV':
        xs=[f'{n}' + (f'×{v}' if v>1 else '') for (kk,n),v in cnt.most_common() if kk==k][:8]
        if xs: parts.append(k+': '+' | '.join(xs))
    print(c,'  '+'  ##  '.join(parts))
