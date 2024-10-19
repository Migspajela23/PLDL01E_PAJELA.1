class Student_Info:

    def __init__(self):
        #initialization
        self.student_name = input("Enter Student Name:")
        self.student_course = input("Enter Student Course:")
        self.student_number = input("Enter Student Number:")
        self.academic_year = input("Enter Academic Year:")
        self.current_date = input("Enter Current Date:")

    #getting subject, section and units

    def getting_subjects(self):
     for i in range(5):
         print(f"Subject {i + 1}")
         subject = input("Enter the Subject")
         section = input("Enter the Sections:")
         unit = int(input("Enter the unit:"))
         self.subject_info_append((subject, section, unit))

    def sum_units(self):
        return sum(unit for _, _, unit in self.subject_info)

class Assesment_Fee:
    def __int__(self):
        self.tuittion_fee_lecture = 1551.0
        self.adU_chronicle = 0
        self.athletic = 0
        self.audio_visual_library = 0
        self.AUSG = 0
        self.cultural_fee
        self.energy_cost_aircon_classroom = 0
        self.guidance = 0
        self.insurance_fee = 0
        self.learning_management_system = 0
        self.library_fee = 0
        self.medical_and_dental = 0
        self.registration = 0
        self.RSO = 0
        self.student_activities_fee = 0
        self.student_nurturance_fee = 0
        self.technology_fee = 0
        self.test_papers = 0

    def get_tuition_fee_lecture(self, units):
        self.tuition_fee_lecture = units * 1551.00

    def get_assessment_amt(self, tuition_fee_lecture, adu_chronicles, athletic, ausg, cultural_fee, energy_cost,
                           guidance, insurance_fee, learning_management_system, library_fee, medical_and_dental,
                           registration, rso, student_activities_fee, student_nurturance_fee, technology_fee,
                           test_papers):
        self.assessment_amt = tuition_fee_lecture + adu_chronicles + athletic + ausg + cultural_fee + energy_cost + guidance + insurance_fee + learning_management_system + library_fee + medical_and_dental + registration + rso + student_activities_fee + student_nurturance_fee + technology_fee + test_papers
        return self.assessment_amt

    def get_total_due(self, assessment_amt, downpayment):
        self.total_due = assessment_amt - downpayment
        return self.total_due






























Student = Student_Info()
Student.subject()
Student.section()
Student.unit()

