'''Copyright (c) 2017 Karan Agrawal
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.'''
   
import sys

def main():
    if len(sys.argv) != 2:
        print("You should provide a cmd line arguments!")
        exit(1)
    
    if sys.argv[1].isalpha() == False:
        print("You should provide valid keyword!")
        exit(1)
        
    message = input("plaintext:  ")
    translated = []
    keyIndex = 0
    keylength = len(sys.argv[1])
    
    for symbol in message:
        if symbol.isalpha():
            key = ord(sys.argv[1][keyIndex % keylength].lower()) - 97
            keyIndex += 1
            translated.append(caesar(symbol, key))
        else:
            translated.append(symbol)
    print("ciphertext: ", end="")
    print("".join(translated))
    exit(0)
    
def caesar(char, key):
    if char.isupper():
        return chr(((ord(char) - 65 + key) % 26) + 65)
    else:
        return chr(((ord(char) - 97 + key) % 26) + 97)

if __name__ == "__main__":
    main()