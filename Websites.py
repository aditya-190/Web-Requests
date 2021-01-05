import webbrowser as browser,time

def Checker(chooser):
    
    if chooser == "Java" or chooser == "java" or chooser == '1':
        browser.open("https://www.geeksforgeeks.org/java/")
        
    elif chooser == "python" or chooser == "Python" or chooser == '2':
        browser.open("https://www.geeksforgeeks.org/python-programming-language/")

    elif chooser == 'c' or chooser == 'C' or chooser == '3':
        browser.open("https://www.geeksforgeeks.org/c-programming-language/")

    elif chooser == 'C++' or chooser == 'c++' or chooser == '4':
        browser.open("https://www.geeksforgeeks.org/c-plus-plus/")
        
    elif chooser == 'swift' or chooser == 'Swift' or chooser == '5':
        print("\n\nSorry Sir! It's Currently Not Available...")
        time.sleep(2)

    elif chooser == 'kotlin' or chooser == 'Kotlin' or chooser =='6':
        browser.open("https://www.geeksforgeeks.org/kotlin-programming-language/")

    elif chooser == 'HTML' or chooser == 'html' or chooser == '7':
        browser.open("https://www.geeksforgeeks.org/html-tutorials/")

    elif chooser == 'css' or chooser == 'CSS' or chooser == '8':
       browser.open("https://www.geeksforgeeks.org/css-tutorials/")

    elif chooser == 'js' or chooser == 'Javascript' or chooser == 'javascript' or chooser == '9':
        browser.open("https://www.geeksforgeeks.org/javascript-tutorial/")

    elif chooser == 'sql' or chooser == 'Sql' or chooser == 'SQL' or chooser == '10':
        browser.open("https://www.geeksforgeeks.org/sql-tutorial/")

    elif chooser == 'Jquery' or chooser == 'jquery' or chooser == '11':
       browser.open("https://www.geeksforgeeks.org/jquery-tutorials/")

    elif chooser == 'php' or chooser == 'PHP' or chooser == '12':
        browser.open("https://www.geeksforgeeks.org/php/")

    elif chooser == 'go' or chooser == 'Go' or chooser == 'golang' or chooser == 'Golang' or chooser == 'GoLang' or chooser == '13':
       browser.open("https://www.geeksforgeeks.org/golang/")

    elif chooser == 'C#' or chooser == 'c#' or chooser == '14':
        browser.open("https://www.geeksforgeeks.org/csharp-programming-language/")

    elif chooser == 'Xml' or chooser == 'xml' or chooser == '15':
       print("\n\nSorry Sir! It's Not Available Currently....")
       time.sleep(2)

    elif chooser == 'coursera' or chooser == 'Coursera' or chooser == '16':
       browser.open("https://www.coursera.org/")        

    elif chooser == 'Hackerearth' or chooser == 'hackerearth' or chooser == '17':
        browser.open("https://www.hackerearth.com/challenges/")

    elif chooser == 'hackerank' or chooser == 'Hackerrank' or chooser == '18':
       browser.open("https://www.hackerrank.com/dashboard")

    elif chooser == 'codechef' or chooser == 'Codechef' or chooser == '19':
       browser.open("https://www.codechef.com/node")

    elif chooser == 'interview' or chooser == 'Interview' or chooser == 'InterviewBit' or chooser == 'interviewbit' or chooser == '20':
        browser.open("https://www.interviewbit.com/practice/")

    elif chooser == 'github' or chooser == 'Github' or chooser == '21':
        browser.open("https://github.com/")

    elif chooser == 'Geeks' or chooser == 'geeks' or chooser == 'GeeksForGeeks' or chooser == 'geeksforgeeks' or chooser == '22':
        browser.open("https://www.geeksforgeeks.org/")

    elif chooser == 'yt' or chooser == 'Youtube' or chooser == 'youtube' or chooser == '23':
        browser.open("https://www.youtube.com/")

    elif chooser == 'Gmail' or chooser == 'gmail' or chooser == '24':
        browser.open("https://mail.google.com/mail/")

    elif chooser == 'drive' or chooser == 'mydrive' or chooser == 'googledrive' or chooser == '25':
        browser.open("https://drive.google.com/drive/")

    elif chooser == 'srm' or chooser == 'erp' or chooser == 'srm erp' or chooser == '26':
        browser.open("https://evarsity.srmist.edu.in/srmsip/")

    else :
        print("\n\nSorry Sir! I Didn't Recognized...")
        time.sleep(2)


print("\n                          I AM HAPPY TO HELP YOU\n\n")
print("\n 1   Java\t\t2   Python\t\t3   C\n 4   C++\t\t5   Swift\t\t6   Kotlin\n 7   HTML\t\t8   CSS\t\t\t9   JavaScript\n 10  SQL\t\t11  Jquery\t\t12  PHP\n 13  GoLang\t\t14  C#\t\t\t15  XML\n--------------------------------------------------------------------------")
print("\n 16  Coursera\t\t17  HackerEarth\t\t18  HackerRank\n 19  Codechef\t\t20  InterviewBit\t21  GitHub\n 22  GeeksForGeeks\n--------------------------------------------------------------------------")
print("\n 23  Youtube\t\t24  Gmail\t\t25  Google Drive\n 26. Srm Erp\n--------------------------------------------------------------------------\n\n")
chooser = input("What Do You Want Me To Do : ")
Checker(chooser)


