import base64 as b64
from json import load as jlf, loads as jls, dump as jdf, dumps as jds

key=[97, 94, 49, 57, 117, 104, 37, 52, 55, 120, 55, 49, 101, 37, 115, 100]

def decode(filename:str):
    l=[]
    with open(f'./{filename}.pcsave','r') as save_file:
        p=0
        while line:=save_file.readline().strip():
            print(f'\npart {p}')
            d=b64.b64decode(line.encode())
            print(f'decoded length: {len(d)}')
            j=bytes([d[i]^key[i%16] for i in range(len(d))])
            print(f'decrypted length: {len(j)}')
            s=jls(j)
            # print(f'json.loads(): {s}')
            l.append(s)
            p+=1
    with open(f'./{filename}.json','w') as json_file:
        jdf(l,json_file)

    # return l

def encode(filename:str):
    with open(f'./{filename}.json','r') as json_file:
        l=jlf(json_file)
    print(f'\nparts count: {len(l)}')
    for p in range(len(l)):
        print(f'\npart {p}')
        part=l[p]
        j=jds(part,separators=(',',':'),ensure_ascii=False).encode()
        d=bytes([j[i]^key[i%16] for i in range(len(j))])
        print(f'encrypted length: {len(d)}')
        s=b64.b64encode(d).decode()
        print(f'encoded length: {len(s)}')
        l[p]=s
    with open(f'./{filename}.pcsave','w') as save_file:
        save_file.write('\n'.join(l))

    # return l

if __name__=='__main__':
    save_name=input('save name ?= ')
    mode=int(input('dec=0, enc=1; ?= '))
    if mode==0:
        decode(save_name)
    elif mode==1:
        encode(save_name)
