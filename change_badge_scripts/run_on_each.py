import os
import time

OLD_BADGE_URL = "https://github.com/adafruit/Adafruit_CircuitPython_Bundle/blob/main/badges/adafruit_discord.svg"
NEW_BADGE_URL = "https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Bundle/main/badges/adafruit_discord.svg"

#path = os.popen('pwd').read()
#print(path.split("/")[-2:])

# checkout main branch
os.system("git checkout main")

# os.system("git pull origin main")

f = open("README.rst", 'r')
readme_str = f.read()
f.close()

if OLD_BADGE_URL in readme_str:
    readme_str = readme_str.replace(OLD_BADGE_URL, NEW_BADGE_URL)
    #print("changed URL, writing...")
    # modify file
    f = open("README.rst", 'w')
    f.write(readme_str)
    f.close()

    # # add readme change
    # os.system("git add README.rst")
    #
    # # make new commit
    # os.system('git commit -m "add docs link to readme"')
    #
    #
    # # push origin main
    # os.system("git push origin main")
    #
    # time.sleep(3)
else:
    print("old badge URL not found")