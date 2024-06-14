import os

path = "sakuranotoki_l10n_cg"
cg=list(filter(lambda x:x.endswith(".png"),os.listdir(path)))
#remove .png extension
cg=list(map(lambda x:x[:-4],cg))
script_path="script"

for fileNm in os.listdir(script_path):
    finalContent=""
    with open(os.path.join(script_path, fileNm), "r",encoding='utf8') as file:
        for line in file:
            if(line.strip().startswith("{\"bg\"")):
                for cgNm in cg:
                    if line.find(cgNm)!=-1:
                        line=line.replace(":cg/",path+"/")
                        break
            finalContent+=line
    with open(os.path.join(script_path, fileNm), "w",encoding='utf8') as file:
        file.write(finalContent)
    print(fileNm)
    
        
        


