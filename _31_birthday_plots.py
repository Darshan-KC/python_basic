# In the previous exercise we counted how many birthdays there are in each month in our dictionary of birthdays.

# In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in! Because it would take a long time for you to input the months of various scientists, you can use my scientist birthday JSON file. Just parse out the months (if you don’t know how, I suggest looking at the previous exercise or its solution) and draw your histogram.

from bokeh.plotting import figure,show,output_file
import _30_birthday_month as ext_file

if __name__ == "__main__":
    output_file("plot.html")

    data = ext_file.readFromFile("birthday.json")
    birthdays = dict()
    # Load our x and y data
    x_categories = list()
    for i in range(1,13):
        x_categories.append(ext_file.numtomonth(i))
        # birthday count 
        count = 0
        for x,y in data.items():
            dob = y.split('/')
            if(i == int(dob[1])):
                count +=1
        birthdays[i] = count
    result = dict()

        
    for x,y in birthdays.items():
        if y > 0:
            index = ext_file.numtomonth(x)
            result[index] = y
    x = [a for a in result.keys()]
    y = [result.get(a) for a in result.keys()]
    
    p = figure(x_range=x_categories)
    p.vbar(x=x, top=y, width=0.5)

    show(p)