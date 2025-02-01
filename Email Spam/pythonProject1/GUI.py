import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import LogisticRegression
import SVM
import DecisionTree
from PIL import ImageTk, Image



def clear_input(input_text):
    input_text.delete(0, END)


def exit_program(window):
    window.destroy()


def secondWindow(selected_classifier, email_input):
    def display_selected_classifier(selection, input_text):

        if selection == "":
            classifier_result_label.config(text="Please select a classifier!", fg="red")
        elif input_text=="":
            classifier_result_label.config(text="Please Enter an Email", fg="red")
        elif selection == "Logistic Regression":
            classifier_result_label.config(text=LogisticRegression.display(), fg="blue")
            spam_result_label.config(text=LogisticRegression.checkSpam(input_text), fg="blue")
        elif selection == "SVM":
            classifier_result_label.config(text=SVM.display(), fg="blue")
            spam_result_label.config(text=SVM.checkSpam(input_text), fg="blue")
        elif selection == "Decision Tree":
            classifier_result_label.config(text=DecisionTree.display(), fg="blue")
            spam_result_label.config(text=DecisionTree.checkSpam(input_text), fg="blue")

    second_window = Toplevel()
    second_window.geometry("500x500")
    second_window.title("Spam Detection")


    exit_button = Button(second_window, text="Exit", command=lambda: exit_program(second_window))
    exit_button.place(x=240, y=400)

    classifier_result_label = Label(second_window, fg="blue", font=14)
    classifier_result_label.place(x=50, y=80)

    spam_result_label = Label(second_window, fg="blue", font=14)
    spam_result_label.place(x=180, y=10)

    display_selected_classifier(selected_classifier, email_input)
    second_window.mainloop()


def firstWindow():
    def get_selected_classifier():
        selected_classifier = classifier_var.get()
        return selected_classifier

    def on_display_outputs():
        selected_classifier = get_selected_classifier()
        email_input = get_email_input()  # Retrieve email input when displaying outputs
        secondWindow(selected_classifier, email_input)

    def get_email_input():
        email_input = email_entry.get()
        return email_input

    first_window = Tk()
    first_window.geometry("500x500")
    first_window.title("Options")

    image = Image.open("OIG2.cvkhpPPkG_WjGqeJZ.jpg")
    photo = ImageTk.PhotoImage(image)

    background_label = Label(first_window, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    welcome_label = Label(first_window, text="Welcome!", font=("Times New Roman", 24), fg="blue")
    welcome_label.place(x=190, y=0)

    classification_label = Label(first_window, text="Enter which classification do you want to use:",
                                 font=("Times New Roman", 18, "bold"), fg="black")
    classification_label.place(x=0, y=50)

    classifier_var = StringVar()
    classifier_label = Label(first_window, text="Select Classifier:", font=("Arial", 12, "bold"))
    classifier_label.place(x=0, y=80)
    classifier_dropdown = OptionMenu(first_window, classifier_var, "Logistic Regression", "SVM", "Decision Tree")
    classifier_dropdown.place(x=150, y=80)

    email_label = Label(first_window, text="Enter the email to check it:", font=("Times New Roman", 24), fg="blue")
    email_label.place(x=70, y=180)

    email_entry = Entry(first_window, font=("Arial", 12), width=30)
    email_entry.place(x=110, y=235, height=40)

    clear_button = Button(first_window, text="Clear", command=lambda: clear_input(email_entry))
    clear_button.place(x=240, y=290)

    display_outputs = Button(first_window, text="Display outputs", command=on_display_outputs,
                             font=("Times New Roman", 20, "bold"))
    display_outputs.place(x=140, y=400)

    first_window.mainloop()


if __name__ == "__main__":
    firstWindow()
