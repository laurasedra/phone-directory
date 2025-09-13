areaCode, prefixNum, lineNum = input().split()
areaCode=int(areaCode)
prefixNum=int(prefixNum)
lineNum=int(lineNum)

print("Country  Phone Number")
print("-------  ------------")
print("U.S.     +1", f"({areaCode}){prefixNum}-{lineNum}")


brazilCode = "+55"
print("Brazil   " + brazilCode, f"({areaCode}){prefixNum + 100}-{lineNum}")

croatiaCode = "+385"
print("Croatia  " +croatiaCode, f"({areaCode}){prefixNum}-{lineNum + 50}")
egyptCode = "+20"
print("Egypt    " +egyptCode, f"({areaCode + 30}){prefixNum}-{lineNum}")
franceCode = "+33"
print("France   " + franceCode, f"({prefixNum}){areaCode}-{lineNum}")


