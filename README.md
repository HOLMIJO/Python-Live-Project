# Python Live Project

## Introduction
For the last two weeks of my time at The Tech Academy, I worked to develop a Web Application in Python/Django focused on weather. It was a great learning opportunity for creating an application from scratch, while adding requested features. I worked on several back end stories that I am very proud of. Over the two week sprint I was exposed to many concepts and methods of programming that I'm confident I will use again and again on future projects.
  
Below are descriptions of some of the stories I worked on, along with code snippets.


### User Creation Function
This allowed the the user to create a profile and saved the user input to the database. 

       def weather_create(request):
    form = UsersForm(request.POST or None) # The form will take the information and POST
    if form.is_valid(): # This checks to see if the form is valid
        form.save() # This will save the information of the user
        return redirect('weather_home')
    else:
        print(form.errors) # If form is invalid or has errors it will print
        form = UsersForm() # Otherwise it will show the form
    context = {
        'form': form
    }
    return render(request, 'WeatherBall/weathercreate.html', context)

 
 ### User Edit Function
In this function the user can click the desired user link on the User Database page and choose "Edit". The user is then brought to a page with the single record and then has the option to edit the record and save or delete the record. 

    def weather_edit(request, pk):
    edit = get_object_or_404(Users, pk=pk) # This will allow the user to edit details of the record
    form = UsersForm(data=request.POST or None, instance=edit)
    if request.method=='POST':
        if form.is_valid(): # If the edited record is valid
            form.save() # The edited information will be saved
            return redirect('weather_home') # Upon saving the updated information user is redirected to the home page.
        else:
            print(form.errors) # If errors or incomplete record
            form = UsersForm() # Return to form
    context = {
        'form': form, 'edit': edit
    }
    return render(request, 'WeatherBall/weatheredit.html', context)

### Web Scraping Function
In this function the user can click the link to the Weather Scraping page. The user is then brought to a page which automatically loads the daily weather forecast including the 7 Day outlook, currently programmed for West Memphis, Arkansas 72301. 

    def weather_edit(request, pk):
    edit = get_object_or_404(Users, pk=pk) # This will allow the user to edit details of the record
    form = UsersForm(data=request.POST or None, instance=edit)
    if request.method=='POST':
        if form.is_valid(): # If the edited record is valid
            form.save() # The edited information will be saved
            return redirect('weather_home') # Upon saving the updated information user is redirected to the home page.
        else:
            print(form.errors) # If errors or incomplete record
            form = UsersForm() # Return to form
    context = {
        'form': form, 'edit': edit
    }
    return render(request, 'WeatherBall/weatheredit.html', context)



### Weather API
In this function the user can click the link to the Weather API page. While the Weather API page does not currently display any weather data on the web page, the requested data including day/s periods does print to the terminal and can be viewed there. The request is currently programmed for West Memphis, Arkansas 72301. 

    def weather_api(request):
    complete_info = []
    not_complete_info = []
    #This is a API link to the National Weather Service detailed forecast for West Memphis, Arkansas 72301
    response = requests.get("https://api.weather.gov/gridpoints/MEG/36,66/forecast")
    sleet = json.loads(response.text)
    wx_properties = sleet['properties']  # this is to go into the properties section of the api
    wx_info = wx_properties['periods']  # we do the same thing with field name seeking forecast
    ''' Here we are doing a for loop to get all of the weather types.
    Made a var assigned as blank string then in for loop we use weather_type to go
    into API and locate the section that has Properties and will then loop through to locate 
    the info in the Periods section. This will loop multiple times to find all results of Periods.
    '''
    for update in wx_info:
        updates = update['name'] #Will give day/s of the week as the result.
        # this is then going to be a var holding our dictionary that is holding the values of the info we got from
        # the above code.
        complete_info.append(updates)
    for i in wx_info:
        temp = i['temperature'] #Will give the daily high and low temperature for the period.
        not_complete_info.append(temp)
      # we then take that info and pass it into our empty list var from the very top
    # and then append the parameter passed in to this to get the string and then use the new info stored inside
    # complete_info and create a for loop in our html to get the info out of it and to be displayed on our api html page.
    print(complete_info)
    print(not_complete_info)
    return render(request, 'WeatherBall/weatherapi.html')


## Other Skills Learned
* Learning from other developers and asking questions as needed.
* Understanding the concepts and methodology for creating an application based on an idea, and being able to design a tangible application and product based on general instructions, and going to work to deliver the requirements according to the specifications given, and gaining acceptance by the Project Manager and Product Owner.
