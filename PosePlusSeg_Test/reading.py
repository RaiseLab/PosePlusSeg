import ast

print('##### readline 함수 #####')
f = open('result2.txt', 'r', encoding='utf-8')
s = f.readlines()
# s = ' '.join(s)
# s = ast.literal_eval(s)
s = str(s)
print(s)
print("      ")
s = s.replace("array","")
# s = s.strip()
s = s.replace("(","")
s = s.replace(")","")
s = s.replace(",\\n'","")
s = s.replace("       [","[")
s = s.replace("'","")
s = s.replace("[[[[","[")
s = s.replace(", ",",")
s = s.replace("]]]\\n]","]")
s = s.replace("[[","[")
s = s.replace("]]","]")
s = s.replace("[","")
s = s.replace("]","")
s = s.replace("\\n'","")
print(s)
f_as = open('result2_out.txt', 'w+t', encoding='utf-8')
f_as.write(s)
f_as.write("\n")
f_as.close()
f.close()