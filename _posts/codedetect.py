import chardet
 
f = open('./2015-11-07-Install Nagios.md')
data = f.read()
print chardet.detect(data)