str1 = "srhb"
str2 = "!req"
str3 = "!req2 | arg1, arg2"
str4 = "!req3 | arg1"
str5 = "!req4 | "
str6 = "!req5 | arg1, arg2, arg4, arg7"
def doThing(r):
    if r[0] == "!":
        r = r.strip("! ").split("|") # format: <request>|<optional arg1>,<optional arg2>,<optional arg3> etc. -> [<request>, <optional args>]
        print(f"Formatted line: {r}")
        rqKW = r[0] # Request keyword = <request> (see above)
        print(f"Keyword: {rqKW}")
        rqArgs = r[1:] # Args = rest of request (though note that this is a list, and not a string)
        print(f"Args (list): {rqArgs}")
        if rqArgs != []:
            rqArgs = rqArgs[0].split(",") # Split the string at index 0 in request args on commas (deals with rqArgs being a list and not a string)
            return rqKW, rqArgs
        else:
            return rqKW
    else:
        return None

if __name__ == "__main__":
    # Test 1:
    a1 = doThing(str1)
    a2 = doThing(str2)
    a3 = doThing(str3)
    a4 = doThing(str4)
    a5 = doThing(str5)
    a6 = doThing(str6)
    print(f"-----\nResults:\n1: {a1}\n2: {a2}\n3: {a3}\n4: {a4}\n5: {a5}\n6: {a6}")
    
    # Test 2:
    print("---------------\ntest 2 (Note: in all cases, strings start after '>' character and end before '<' to make whitespace clearer):")
    s = "!abcde|fgh"
    s2 = "!abcde | fgh"
    print(f"-----\nS: >{s}<\nS2 (with spaces): >{s2}<")
    s = s.strip("! ")
    s2 = s2.strip("! ")
    # s = s.strip("!").strip(" ")
    # s2 = s2.strip("!").strip(" ")
    print(f"-----\nStrings w/ chars removed:\nS: >{s}<\nS2: >{s2}<")
    s = s.split("|")
    s2 = s2.split("|")
    print(f"-----\nSplit strings:\nS: >{s}<\nS2: >{s2}<")
    print("Error (test 2): python not removing spaces from strings via .strip()")