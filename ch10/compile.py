with open('mymodule.py') as f:
     lines = f.read()

code_obj = compile(lines, 'mymodule.py', 'exec')
exec(code_obj)
