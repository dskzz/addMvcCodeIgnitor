import sys
import shutil
import os


class MvcAdd:
    incNav = None
    incJs = None
    pathList = None
    skelList = None
    fullPathFileList = None
    regexList = None
    nameList = None
    api = None

    def __init__(self, name, incNav, incJs, api):
        self.theName = name

        if incNav.lower().rstrip() == 'y':
            self.incNav = True

        if incJs.lower().rstrip() == 'y':
            self.incJs = True

        self.api = api

        self.initPathList()

    def initPathList(self):
        n = self.theName
        self.nameList = {
            'controller':  n + ".php",
            'model':  n + "_model.php",
            'view_dir':  n.lower() + '/',
            'view':  n.lower() + '.tpl',
            'view_nav':  n.lower() + "_nav.tpl",
            'script_ts':  n.lower() + ".ts",
            'script_js':  n.lower() + ".js"
        }

        if self.incJs is False:
            self.nameList['script_js'] = ''

        self.pathList = {
            'controller': 'controllers/',
            'model': 'models/',
            'view': 'views/templates/panels/' + self.nameList['view_dir'],
            'view_nav': 'views/templates/panels/' + self.nameList['view_dir'],
            'script_ts': '../scripts-dev/',
            'script_js': '../scripts/'
        }

        self.skelList = {
            'controller': 'skel/controller.php',
            'controller_api': 'skel/controller_api.php',
            'model': 'skel/model.php',
            'view': 'skel/view.tpl',
            'view_nav': 'skel/nav.tpl',
            'script_ts': 'skel/script.ts_'
        }

        self.fullPathFileList = {
            'controller_api': 	self.pathList['controller'] + self.nameList['controller'],
            'controller': 	self.pathList['controller'] + self.nameList['controller'],
            'model': 	self.pathList['model'] + self.nameList['model'],
            'view': 	self.pathList['view'] + self.nameList['view'],
            'view_nav': 	self.pathList['view_nav'] + self.nameList['view_nav'],
            'script_ts': 	self.pathList['script_ts'] + self.nameList['script_ts'],
            'script_js': 	self.pathList['script_js'] + self.nameList['script_js']
        }

        self.regexList = {
            'controller':	 "s/CONTROLLERNAMEHERE/" + n + "/g",
            'controller_api':	 "s/CONTROLLERNAMEHERE/" + n + "/g",
            'model':	 "s/MODELNAMEHERE/" + n.lower() + "_model/g",
            'view':	 "s/VIEWNAMEHERE/" + n.lower() + "/g",
            'script_ts':	 "s/VIEWNAMEHERE/" + n + "/g",
            'script_include':	 "s/QUOTESCRIPTNAMEHERE/\"" + self.nameList['script_js'] + "\"/g",
            'lower':	 "s/LOWERNAMEHERE/" + n.lower() + "/g"

        }

    def createViewPath(self):
        try:
            os.makedirs(self.pathList['view'], False)

        except:
            pass

        print("# chmod 775 " + self.pathList['view'])
        os.chmod(self.pathList['view'], 0o775)

    def doCopy(self, indexName):
        print("# copy %s to %s " %
            (self.skelList[indexName], self.fullPathFileList[indexName]))
        shutil.copyfile(self.skelList[indexName],
                        self.fullPathFileList[indexName])

    def doSed(self, regexIndex, pathIndex=None):
        if pathIndex is None:
            pathIndex = regexIndex
        cmd = "sed -i '%s' %s" % (self.regexList[regexIndex],
                                    self.fullPathFileList[pathIndex])
        print("# " + cmd)
        os.system(cmd)


    def doIt_api(self):
        print("COPY MVC")
        self.doCopy('controller_api')
        self.doCopy('model')

        print("EDITING MVC")
        self.doSed('controller_api')

        self.doSed('lower', 'controller_api')
        self.doSed('model', 'controller_api')
        self.doSed('model')

        del self.fullPathFileList['script_js']
        del self.fullPathFileList['view']
        del self.fullPathFileList['view_nav']
        del self.fullPathFileList['script_ts']

        print("COMPLETE")

        print(" ")

    def doIt(self):
        print("CREATE VIEW PANEL FOLDER")
        self.createViewPath()

        print("COPY MVC")
        self.doCopy('controller')
        self.doCopy('model')
        self.doCopy('view')

        print( "")
        print("EDITING MVC")
        self.doSed('controller')
        self.doSed('script_include', 'controller')
        self.doSed('lower', 'controller')
        self.doSed('model', 'controller')

        self.doSed('model')
        self.doSed('view')
        print("")

        if self.incNav:
            print("INCLUDE NAV")
            self.doCopy('view_nav')
            print(" ")

        if self.incJs:
            print("INCLUDE SCRIPT")
            self.doCopy('script_ts')
            self.doSed('script_ts')
            print("")

        print("COMPLETE.  Don't forget to change navigation table in the database for left column page nav.")

        print(" ")

    def printDelete(self):
        for item in self.fullPathFileList:
            print("rm " + self.fullPathFileList[item])

        if not self.api:
            print("rmdir " + self.pathList['view'])


#################################################

cli_args = sys.argv
cli_args.pop(0)


def prompt( cli_args=None ):
	if len(cli_args) > 0:
		nameOfMVC = cli_args.pop(0)
	else:
		nameOfMVC = input("Please enter name of MVC> ")

	if len(cli_args) > 0 and cli_args[0] == 'api':
		includeName = nameOfMVC
		includeTS = 'n'
		includeNav = 'n'
		api = 'y'
		return (includeName, includeTS, includeNav, api)
	else:
		api = input( "API? (No view) Y/N> ")

	if api :
		includeName = nameOfMVC
		includeTS = 'n'
		includeNav = 'n'
		api = 'y'
		return (includeName, includeTS, includeNav, api)

	if len(cli_args) > 0:
		includeNav = cli_args.pop(0)
	else:
		includeNav = input("Include Navbar on panel? Y/N> ")

	if len(cli_args) > 0:
		includeTS = cli_args.pop(0)
	else:
		includeTS = input("Include JS (typescript actually) file? Y/N> ")


	# Default
	if includeNav.lower().rstrip() != 'n':
		includeNav = 'y'

	if includeTS.lower().rstrip() != 'n':
		includeTS = 'y'

	return (includeName, includeTS, includeNav, 'n')


(nameOfMVC, includeTS, includeNav, api) = prompt(cli_args)
newMvc = MvcAdd(nameOfMVC, includeNav, includeTS, api)

if api:
	newMvc.doIt_api()
else:
	newMvc.doIt()

print("DELETION: ")
newMvc.printDelete()
print("\nDONE\n")
