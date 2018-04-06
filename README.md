# quikchex-attendancemark
## Mark the attendance in quikchex portal Automatically

**Dependencies**
  - Python2.7
  - Selenium - pip install selenium
  - Chromium Driver - brew install chromedriver (if already installed, add it to path - export PATH=$PATH:/path/to/chromedriver/folder)

**Run** -
 /path-to-python-executable /path-to-qc.py {quikchex username} {quikchex password} 
 > Example -> python /Users/rv/qc.py rakesh.verma@pharmeasy.in hahahahahaha

> Expected Response Time => 30 Seconds.

*The Script will launch a chrome instance and would log you into your quikchex portal and Mark attendance for you.*

**Feel free to Star and open any issues in case of any unexpected response.**

- PS: Add it to your bash profile for faster attendance marking.
- Add the following command to your crontab ( `crontab -e` ) to run it automatically every day :P
 0 10-19 * * 1-5 python /path-to-qc.py {username} {password} to run it at 10 in the morning and 7 in the evening everyday from Monday to Friday. (Only for educational Purpose)
