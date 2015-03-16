# HTML_generator
def generate_concept_HTML(title1, description):
    html_text_1 = '''
<div class="notes">
    <h2 class="title1">''' + title1
    html_text_2 = '''
    </div>
    <div class="description">''' + description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    title1 = concept[0]
    description = concept[1]
    return generate_concept_HTML(title1, description)

EXAMPLE_LIST_OF_CONCEPTS = [ ['Serious Programming', '<p>A computer can be <b>programmed</b> to do anything we want, as lng as we can write a program that specifies a <i>specific sequence of instructions</i>. A program is a precise sequence of steps that a computer can follow to do something useful.  Web browsers, games, mobile apps, and simple print statements are all examples of computer programs. A <b>Programming Language</b> is what programmers use to tell a computer what to do.  <i><b>Python</b></i> is one example of a programming language.</p><p>When you write Python code press "Run",a <i>Python Interpreter</i> converts the code you wrote as a set of instuctions that the computer itself can understand and execute.</p>'],
                             ['Variables and Srings What is a <b>variable</b> in Python?', '<p>In programming, a variable is a value that can change, depending on conditions or on information passed to the program. Typically, a program consists of instructions that tell the computer what to do and data that the program uses when it is running.Variables give programmers a way to give <i>names</i> to values. For example <b>my_variables</b> is a variable with the value of <b>2</b>, then the following code would print out <b>4</b>:<br> <b>print my_variable + my_variable</b></p><p>In computer programming, a string is traditionally a sequence of characters, either as a literal constant or as some kind of variable. The latter may allow its elements to be mutated and the length changed, or it may be fixed (after creation).</p>'],
                             ['Input -> Function -> Output', '<p>A function is something that takes input, does something to that input, and then produces output.  For example, a function named <b>square</b> might take a number as input and produce the square of that number as output.  Functions are made by stating a line of code with the <b>def</b> and then giving a function namefollowed by the function <b>parameter</b> in parentthesis.  These parameters will eventually be replaced by the actual values when the function is used.</p><p>In the "body" of the function, we write code that specifies what to do with the input parameters.  For example the following code could be the definition of a function called <b>square</b>:<br>def square(x): <br> answer = x + x <br> return answer</p>']]


def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)