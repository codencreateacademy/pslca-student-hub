from pathlib import Path
import shutil

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'Website'
OUT=ROOT/'_site'
OUT.mkdir(exist_ok=True)

def copy(source,relative):
    destination=OUT/relative
    destination.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(source,destination)

for path in SOURCE.rglob('*'):
    if path.is_file() and (path.suffix.lower() in {'.html','.css','.json'} or path.name=='.nojekyll'):
        copy(path,path.relative_to(SOURCE))

allowed={'.pdf','.png','.svg','.jpg','.jpeg','.webp','.gif','.md'}
for name in ['Grades_5-6','Grades_7-8','Grades_9-10','Shared_Resources']:
    for path in (ROOT/name).rglob('*'):
        if path.is_file() and path.suffix.lower() in allowed:
            copy(path,path.relative_to(ROOT))
copy(ROOT/'README.md',Path('README.md'))
assert (OUT/'index.html').is_file()
assert (OUT/'Shared_Resources/Voltage_Lab/presentations.html').is_file()
print('Prepared student website in',OUT)
