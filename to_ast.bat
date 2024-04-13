git submodule init
git submodule update
python to_script.py

cd ./VNTextPatch
VNTextPatch insertlocal ..\script_jp ..\translated_local ..\script --format=artemisast
cd ..

python replace_cn_cg_path.py