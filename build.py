from pathlib import Path
import json
root=Path(__file__).resolve().parent
s=(root/'src/page.html').read_text()
for name,file in [('QUESTIONS','questions'),('LESSONS','lessons'),('EXPLANATIONS','extras')]:
 s=s.replace('__'+name+'__',json.dumps(json.loads((root/f'src/{file}.json').read_text()),ensure_ascii=False).replace('</','<\\/'))
(root/'index.html').write_text(s)
print('index.html erstellt')
