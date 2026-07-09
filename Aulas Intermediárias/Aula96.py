import sys

platform = 'A MINHA'
print(sys.platform)
print(platform)





import sys as s

sys = 'alguma coisa'
print(s.platform)
print(sys)






from sys import platform as pf, exit as ex

print(pf)
print(ex)





from sys import * #má pratica

print(platform)
exit()