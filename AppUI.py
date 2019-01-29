from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk

class AppUI(Frame):

    def __init__(self, root=None):
        Frame.__init__(self, root, relief=SUNKEN, bd=1)

        root.title('Automata')
        root.geometry('{}x{}'.format(1100, 600))
        root.configure()
        self.answer = IntVar()

        # Menu bar
        self.menubar = Menu(root)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label='Open', command=self.open_file_function, accelerator='Ctrl+O')
        filemenu.add_command(label='Save Graph', command=self.open_file_function, accelerator='Ctrl+G')
        filemenu.add_command(label='Save File', command=self.open_file_function, accelerator='Ctrl+S')
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=root.quit, accelerator='Ctrl+Q')
        self.menubar.add_cascade(label='File', menu=filemenu)


        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            self.master.tk.call(root, 'config', '-menu', self.menubar)

        # Frames
        self.options_frame = Frame(width=1100, height=30, relief=SUNKEN, bd=2)
        self.options_frame.pack(side='top', fill='x')

        self.automaton_left_frame = Frame(width=300, height=200, relief=SUNKEN, bd=1)
        self.automaton_left_frame.pack(side='left', anchor=N, fill='x')

        self.automaton_right_frame = Frame(relief=SUNKEN, bd=2)
        self.automaton_right_frame.pack(side='right', anchor=N, fill='x')

        self.graph_frame = Frame(relief=SUNKEN, bd=2)
        self.graph_frame.pack(fill='both', expand=True)

        self.regex_frame = Frame(height=200, relief=SUNKEN, bd=2)
        self.regex_frame.pack(side='bottom', fill='x')

        self.initial_gui_componenets()

        self.add_state_members()

    def add_state_members(self):
        self.lbxStates.insert(self.lbxStates.size(), 'Ze magic row 1')
        self.lbxStates.insert(self.lbxStates.size(), 'Ze faggot row 2')
        self.lbxStates.insert(self.lbxStates.size(), 'Ze sexay row 3')

    def open_file_function(self):
        root = Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename()

    def change_state(self):
        self.ibRegex['state'] = self.state

        self.btGenerate.config(state=self.state)

    def regex_checked(self, event):
        if self.answer.get() == 0:
            self.state = 'normal'
            self.change_state()
        else:
            self.state = 'disabled'
            self.change_state()
        self.update()

    def check_if_finite(self):
        if self.lbFinite['text'] == 'y':
            self.state = 'normal'
            self.change_validate()
        else:
            self.state = 'disabled'
            self.change_validate()
        self.update()

    def change_validate(self):
        self.lbValidate.config(state=self.state)
        self.ibValidate.config(state=self.state)
        self.btValidate.config(state=self.state)
        self.lbRegex.config(state=self.state)
        self.lbValidateList.config(state=self.state)
        self.ibxWords.config(state=self.state)

    def initial_gui_componenets(self):
        lbHeadin = Label(self.options_frame, text='You can open a file from "File" menu or by using Ctrl + O command!')
        lbHeadin.pack(side=TOP, anchor=W)

        c = Checkbutton(self.options_frame, text='Load from automaton regex',
                        variable=self.answer, onvalue=True, offvalue=False)
        c.pack(side=TOP, anchor=W)
        c.bind('<Button-1>', self.regex_checked)

        lbDetails = Label(self.options_frame, text='Automaton details:')
        lbDetails.pack(side=TOP, anchor=W)

        lbDetails1 = Label(self.automaton_left_frame, text='Alphabet:')
        lbDetails1.grid(row=0, column=0, sticky=W)

        lbAlphabet = Label(self.automaton_left_frame, text='alphabet here')
        lbAlphabet.grid(row=0, column=1)

        lbDetailsST = Label(self.automaton_left_frame, text='States:')
        lbDetailsST.grid(row=1, column=0, sticky=W)

        self.lbxStates = Listbox(self.automaton_left_frame, width=30, height=8)
        self.lbxStates.grid(row=2, column=0)

        lbDetailsSTedges = Label(self.automaton_left_frame, text='Edges of selected state:')
        lbDetailsSTedges.grid(row=1, column=1, sticky=W)

        self.lbxEdges = Listbox(self.automaton_left_frame, height=8)
        self.lbxEdges.grid(row=2, column=1)

        lbDetailsFinal = Label(self.automaton_left_frame, text='Final:')
        lbDetailsFinal.grid(row=3, column=0, sticky=W)

        selflbFinal = Label(self.automaton_left_frame, text='final here')
        selflbFinal.grid(row=3, column=1)

        lbDetailsInitial = Label(self.automaton_left_frame, text='Initial:')
        lbDetailsInitial.grid(row=4, column=0, sticky=W)

        self.lbInitial = Label(self.automaton_left_frame, text='initial here')
        self.lbInitial.grid(row=4, column=1)

        lbDetails2 = Label(self.automaton_left_frame, text='Transitions:')
        lbDetails2.grid(row=5, column=0, sticky=W)

        self.listboxTransitions = Listbox(self.automaton_left_frame, width=30)
        self.listboxTransitions.grid(row=6, column=0, sticky=W)

        lbDetailsFinite = Label(self.automaton_left_frame, text='is Finite:')
        lbDetailsFinite.grid(row=7, column=0, sticky=W)

        self.lbFinite = Label(self.automaton_left_frame, text='y/n')
        self.lbFinite.grid(row=7, column=1)

        lbDetailsFinite = Label(self.automaton_left_frame, text='is PDA:')
        lbDetailsFinite.grid(row=8, column=0, sticky=W)

        self.lbFinite = Label(self.automaton_left_frame, text='y/n')
        self.lbFinite.grid(row=8, column=1)

        lbDetailsNFA = Label(self.automaton_left_frame, text='is NFA:')
        lbDetailsNFA.grid(row=9, column=0, sticky=W)

        self.lbNFA = Label(self.automaton_left_frame, text='y/n')
        self.lbNFA.grid(row=9, column=1)

        lbIfFile = Label(self.automaton_left_frame, text='If automaton from file:',)
        lbIfFile.grid(column=0, row=10, sticky=W)

        btValidateFile = Button(self.automaton_left_frame, text='Compare results to test data!')
        btValidateFile.grid(column=0, row=11, sticky=W)

        self.leftFrame = Frame(self.regex_frame, relief=SUNKEN, bd=2)
        self.leftFrame.pack(side='left', anchor=N, fill='y')

        self.rightFrame = Frame(self.regex_frame, relief=SUNKEN, bd=2)
        self.rightFrame.pack(side='right', anchor=N, fill='both', expand=True)

        self.state = 'disabled'

        self.lbValidate = Label(self.leftFrame, text='Validate word:', state=self.state)
        self.lbValidate.grid(column=0, row=0, sticky=W)

        self.ibValidate = Entry(self.leftFrame, width=40, state=self.state)
        self.ibValidate.grid(column=0, row=1)

        self.btValidate = Button(self.leftFrame, text='Validate', state=self.state)
        self.btValidate.grid(column=1, row=1)

        self.lbRegex = Label(self.leftFrame, text='Enter regex:', state=self.state)
        self.lbRegex.grid(column=0, row=2, sticky=W)

        self.ibRegex = Entry(self.leftFrame, width=40, state=self.state)
        self.ibRegex.grid(column=0, row=3)

        self.btGenerate = Button(self.leftFrame, text='Generate', state=self.state, command=self.check_if_finite)
        self.btGenerate.grid(column=1, row=3)

        self.lbValidateList = Label(self.rightFrame, text='List of words if automaton is finite:', state=self.state)
        self.lbValidateList.grid(column=0, row=0, sticky=W)

        self.ibxWords = Listbox(self.rightFrame, width=86, state=self.state)
        self.ibxWords.grid(column=0, row=1)

        # Canvas
        c = Canvas(self.graph_frame, bg='white', width=825)
        c.pack()
        photo = Image.open('img.png')
        self.update()
        photo = photo.resize((825, c.winfo_height()), Image.ANTIALIAS)
        photo.save('resized_img.jpg')
        c.image = ImageTk.PhotoImage(photo)
        c.create_image(0, 0, image=c.image, anchor='nw')

root = Tk()

app = AppUI(root)
app.pack()

root.mainloop()
