from School import School, ClassRoom, Subject
from Person import Student, Teacher
def main():
    # print('main is running')

    school = School('Adam jee','U tt ara')

    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    abul = Student('abul khan',eight)
    school.student_admission(abul)
    babul = Student('babul khan',eight)
    school.student_admission(babul)
    cabul = Student('kabul khan',eight)
    school.student_admission(cabul)

    #subjects
   
    physics_teacher = Teacher('Shahjahan Tapon Rana')
    physics = Subject('physics',physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher('haradhon nag')
    chemistry = Subject('chemistry',chemistry_teacher)
    eight.add_subject(chemistry)

    Biology_teacher = Teacher('ajmal sir')
    Biology = Subject('Biology',Biology_teacher)
    eight.add_subject(Biology)

    print(school)


if __name__ =='__main__':
    main()