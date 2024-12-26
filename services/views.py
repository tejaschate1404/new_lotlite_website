from django.shortcuts import render ,get_object_or_404
from django.shortcuts import render, redirect
from .models import StudentMobilityCourse
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required


# Create your views here.
def services(request):
    return render(request,"services2.html")

def details_Web_Development(request):
    return render(request,"Web_Development.html")




 # Pass the courses to the template
def studentMobility(request):
    courses = StudentMobilityCourse.objects.all()
    
    # Pass the courses to the template
    return render(request, 'studentMobility.html', {'courses': courses})


def student_mobility_course_detail(request, course_id):
    # Fetch the specific course by ID
    course = get_object_or_404(StudentMobilityCourse, pk=course_id)
    
    # Pass the course data to the template
    return render(request, 'student_mobility_course_detail.html', {'course': course})



class AddStudentMobilityView(View):
    template_name = 'add_services.html'  # Template to render the form

    def get(self, request):
        # Render the form page
        return render(request, self.template_name)

    def post(self, request):
        # Handle form submission
        background_photo = request.FILES.get('image')
        title = request.POST.get('title')
        title_heading_details = request.POST.get('title_heading_details')
        description = request.POST.get('desc')
        courses_included = request.POST.get('courses_include')
        course_contents = request.POST.get('course_contents')
        course_trainer = request.POST.get('course_trainer')
        start_date = request.POST.get('start_date')
        duration = request.POST.get('duration')
        price = request.POST.get('price')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image1_description = request.POST.get('image1_discription')
        image2_description = request.POST.get('image2_discription')
        image3_description = request.POST.get('image3_discription')

        # Create and save the new StudentMobilityCourse object
        student_course = StudentMobilityCourse(
            background_photo=background_photo,
            title=title,
            title_heading_details=title_heading_details,
            description=description,
            courses_included=courses_included,
            course_contents=course_contents,
            course_trainer=course_trainer,
            start_date=start_date,
            duration=duration,
            price=price,
            image1=image1,
            image2=image2,
            image3=image3,
            image1_description=image1_description,
            image2_description=image2_description,
            image3_description=image3_description
        )
        student_course.save()

        # Redirect to the same page after successful save
        return redirect('view_student_mobility')







def view_student_mobility(request):
    courses = StudentMobilityCourse.objects.all()
    return render(request, 'view_service.html', {'courses': courses} )


def update_course(request, course_id):
    course = get_object_or_404(StudentMobilityCourse, id=course_id)
    
    if request.method == 'POST':
        # Update course fields with POST data
        course.title = request.POST['title']
        course.title_heading_details = request.POST['title_heading_details']
        course.description = request.POST['description']
        course.courses_included = request.POST['courses_included']
        course.course_contents = request.POST['course_contents']
        course.course_trainer = request.POST['course_trainer']
        course.start_date = request.POST['start_date']
        course.duration = request.POST['duration']
        course.price = request.POST['price']

        # Handle images (if new images are uploaded)
        if request.FILES.get('background_photo'):
            course.background_photo = request.FILES['background_photo']
        if request.FILES.get('image1'):
            course.image1 = request.FILES['image1']
        if request.FILES.get('image2'):
            course.image2 = request.FILES['image2']
        if request.FILES.get('image3'):
            course.image3 = request.FILES['image3']

        # Update image descriptions
        course.image1_description = request.POST['image1_description']
        course.image2_description = request.POST['image2_description']
        course.image3_description = request.POST['image3_description']

        # Save the updated course
        course.save()

        return redirect('view_student_mobility')  # Redirect after saving

    return render(request, 'update_course.html', {'course': course})

def delete_course(request, course_id):
    course = get_object_or_404(StudentMobilityCourse, id=course_id)
    course.delete()
    return redirect('view_student_mobility')


def view_course(request, course_id):
    course = get_object_or_404(StudentMobilityCourse, id=course_id)
    if request.method == 'POST':
        # Get data from the form
        course.background_photo = request.FILES.get('background_photo', course.background_photo)
        course.title = request.POST['title']
        course.title_heading_details = request.POST['title_heading_details']
        course.description = request.POST['description']
        course.courses_included = request.POST['courses_included']
        course.course_contents = request.POST['course_contents']
        course.course_trainer = request.POST['course_trainer']
        course.start_date = request.POST['start_date']
        course.duration = request.POST['duration']
        course.price = request.POST['price']

        # Handle images (if new images are uploaded)
        if request.FILES.get('image1'):
            course.image1 = request.FILES['image1']
        if request.FILES.get('image2'):
            course.image2 = request.FILES['image2']
        if request.FILES.get('image3'):
            course.image3 = request.FILES['image3']

        course.image1_description = request.POST['image1_description']
        course.image2_description = request.POST['image2_description']
        course.image3_description = request.POST['image3_description']

        # Save the updated course
        course.save()

        return redirect('view_student_mobility')
    return render(request, 'view_course.html', {'course': course})





   