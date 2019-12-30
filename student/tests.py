from django.test import TestCase,Client

from .models import Student

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='the5fire',
            sex=1,
            email='nobody@the5fire.com',
            profession='程序员',
            qq='666666',
            phone='88888888',
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='pengrui',sex=1,email='nobody@dd.com',profession='程序员',qq='666666',phone='88888888',
        )
        self.assertEquals(student.sex_show,'男','性别字段内容与展示不一致！')

    def test_filter(self):
        Student.objects.create(
            name='pengrui',sex=1,email='nobody@dd.com',profession='程序员',qq='666666',phone='88888888',
        )
        name='the5fire'
        students = Student.objects.filter(name=name)
        self.assertEquals(students.count(),1,'应该只存在为{}的记录'.format(name))


def test_get_index(self):
    client = Client()
    responese = client.get('/')
    self.assertEquals(responese.status_code,200,'status code must be 200!')

def test_post_student(self):
    client = Client()
    data = dict(
        name = 'test_for_post',
        sex = 1,
        email = '333@dd.com',
        profession = '程序员',
        qq = '666666',
        phone = '88888888',
    )
    response = client.post('/',data)
    self.assertEquals(response.status_code, 302,'status code must be 302!')

    response = client.get('/')
    self.assertTrue(b'test_for_post' in response.content,'response content must contain `test_for_post`')
