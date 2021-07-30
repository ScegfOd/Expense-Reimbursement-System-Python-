from subprocess import call
def resetdb():
	call("cd db_init && ./reset.sh", shell=True)

if __name__=='__main__':
	resetdb()
