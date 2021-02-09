import sys
import os

def main(argv):
	ip = argv[2]
	port = argv[3]
	shell_file = os.path.expanduser('~') + "/usr/share/shells/templates/" + argv[1]

	try:
		f = open(shell_file, "r")

	except:
		print("error: shell template " + shell_file + " not found")

	shell = f.read()

	shell =	shell.replace('x.x.x.x', ip)
	shell = shell.replace('yyyy', port)

	print(shell)













if __name__ == "__main__":
	if(len(sys.argv) == 4):
		main(sys.argv)
	else:
		print("useage: shell.py <shell_type> <ip> <port>")

