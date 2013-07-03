#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with rub-login.  If not, see <http://www.gnu.org/licenses/>.
import urllib, string, time, os, sys, platform, re, urllib2, cookielib
def login(username, password):
  link_login = "https://login.rz.ruhr-uni-bochum.de/cgi-bin/laklogin"
  #if int(platform.python_version()[:1]) == 3:
  #  import urllib.request, urllib.error, urllib.parse, http.cookiejar
  #  login_data = urllib.parse.urlencode({'action': 'Login', 'username' : username, 'password' : password})
  #  cj = http.cookiejar.CookieJar()
  #  opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
  #else:
  login_data = urllib.urlencode({'action': 'Login', 'loginid' : username, 'password' : password})
  cj = cookielib.CookieJar()
  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) 
  opened = opener.open(link_login, login_data)

  message = opened.read().splitlines()
  for line in message:
    if line.startswith("<font face=\"Helvetica, Arial, sans-serif\"><big>"):
      p = re.compile(r'<.*?>')
      if p.sub('', line) == "Authentisierung gelungen":
        # Authentification was successful
        return True 
      else:
        # Authentification failed
        return False

def logout():
  link_logout = "https://login.rz.ruhr-uni-bochum.de/cgi-bin/laklogin"
  logout_data = urllib.urlencode({'action': 'Logout'})
  cj = cookielib.CookieJar()
  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
  opened = opener.open(link_logout, logout_data)
