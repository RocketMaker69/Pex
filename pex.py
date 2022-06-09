class PexEngine:
	def Build(self, file: str, offset: int = 5):
		code = open(file, "r").read()
		newc = ""
		
		assert offset < 11, "Cannot offset more than 10."
		newc += f"{offset}:"

		for char in code:
			n = ord(char) + offset if ord(char) + offset <= 127 else ord(char) + offset - 127
			newc += chr(n)
		
		out = open(file[:-2] + "pex", "w")
		out.write(newc)


	
	def Run(self, file: str):
		code = open(file, "r").read()
		newc = ""

		offset = int(code[:code.find(":")])

		for char in code[code.find(":")+1:]:
			n = ord(char) - offset if ord(char) - offset >= 0 else ord(char) - offset + 127
			newc += chr(n)
		
		exec(newc + f"\n\ninput(\"\\nPress enter to exit...\")")



	def Debuild(self, file: str):
		code = open(file, "r").read()
		newc = ""

		offset = int(code[:code.find(":")])
		print(offset)

		for char in code[code.find(":")+1:]:
			n = ord(char) - offset if ord(char) - offset >= 0 else ord(char) - offset + 127
			newc += chr(n)
		
		print(newc)