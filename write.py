f = open("newfile.txt","a")
lines = ["hello","world","welcome","to","file IO"]
text = "\n".join(lines)

f.writelines(text)
f.close()
