
def Featured_Courses_header(headername):
    return "//h1[text()='" +headername+ "']"

def Featured_Courses_subtext(subtext):
    return "//div[contains(text()='"+subtext+"')]"

def Featured_Courses1_Title(position):
    return "//div[@class='col-lg-9']/div/div["+position+"]/div/div[1]//h5/a"

def Featured_Courses1_Duration(duration):
    return "//div[@class='col-lg-9']/div/div["+duration+"]/div/div[1]/div/div[1]"

def Featured_Courses1_Class(class1):
    return "//div[@class='col-lg-9']/div/div["+class1+"]/div/div[1]/div/div[2]/span"