import vk
import random


class Mixim(object):
    kafedra = ("радиофизика",
               "радиофизика",
               "наноэлектроника",
               "програмирования",
               "технофизика")
    degree = ("кандидат наук", "доктор наук")

    endName = '''Данилевна
Антониновна
Тимофеевна
Кириллович
Мечиславович
Елизарович
Мечиславович
Юлиевна
Прокофиевич
Андрияновна
Алексеевич
Михеевна
Станиславовна
Анатолиевна
Афанасиевна
Глебович
Самсонович
Леонтиевич
Игоревич
Эрнстович'''
    rPath = ("Test", "dock")

    def _getKafedra(self):
        return random.choice(self.kafedra)

    def _getEndname(self):
        return random.choice(self.endName.replace('\t', '').split("\n"))

    def _getDeegree(self):
        return random.choice(self.degree)

    def _getBookCheck(self):
        return "{}-{}".format(random.randint(10000000, 99999999), random.choice(("ДФ", "ФС", "БС")))

    def _getFNAME(self):
        return "{}.pdf".format(random.randint(100, 100000))

    def _getFPasth(self, name):
        return "/{}/{}/{}.pdf".format(random.randint(100, 100000), random.choice(self.rPath), name)

    def _getFullPath(self):
        gen = self._getFNAME()
        return ("/{}/{}/{}.pdf".format(random.randint(100, 100000), random.choice(self.rPath), gen), gen)

    def _getCom(self):
        return  random.randint(0, 2000)


class genTable(Mixim):
    vk_autch = {
        'myLogin': '*',
        'myPassword': '****',
        'myApp_id': "**",
        'v': '5.103'
    }
    vk_api = None

    def __init__(self, dicts="фапрсдл"):
        self.vk_start()
        self.dicts = dicts  # use created search reqwest arg[q]

    def createStudent(self):
        for f, s in self.__gen():
            yield (self._getBookCheck(), f, s, self._getEndname(), self._getKafedra())

    def createTeachers(self, coint):
        for f, s in self.__gen(coint):
            yield (f, s, self._getEndname(), self._getKafedra(), self._getDeegree())

    def vk_start(self):
        session = vk.AuthSession(app_id=self.vk_autch['myApp_id'], user_login=self.vk_autch['myLogin'],
                                 user_password=self.vk_autch['myPassword'])
        self.vk_api = vk.API(session, v=self.vk_autch['v'], lang='ru')
        return 0

    def __gen(self, myCount=400):
        genList = []  # return res reqwest type:list
        for i in self.dicts:
            genList += [(i['first_name'], i['last_name']) for i in
                        self.vk_api.users.search(q=i, sort='1', count=str(400))['items'] if
                        len(i['last_name']) > 5 and len(i['first_name']) > 2]
        return genList
