def num_obj(s):
   array = []
   for i in range(len(s)):
       object = {}
       object[str(s[i])] = chr(int(s[i]))
       array.append(object)
   print(array)
   return array

