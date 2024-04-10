import urllib.robotparser as robpsr

par = robpsr.RobotFileParser()
par.set_url('https://www.samsclub.com/robots.txt')
par.read()
print(par)

print(par.can_fetch('*', 'https://www.samsclub.com/category'))
