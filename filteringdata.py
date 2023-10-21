from transformers import pipeline
def filterdata(filename,query,outputfilename):
    with open(filename,'r') as f:
        content = f.read()
    for i in range(0,len(content)-701,600):
        inputstr = content[i:i+700]
        text = "Returning Non Redundant Information from Input that is relevant to query   Input:{}    Query:{} Output:".format(inputstr,query)
        text_generation = pipeline("text-generation", model='gpt2')
        generated_text= text_generation(text, max_length=300, do_sample=False)[0]
        output = generated_text['generated_text']
        with open(outputfilename,'a+') as f:
            f.write(str(output[len(text):]))
    
def info(filename, query, outputfilename):
    temp = filename[:-5]+'temp.txt'
    with open(temp,'w') as f:
        f.write('query = {}'.format(query))
    filenamenow = filename
    for i in range(5):
        print(i)
        filterdata(filenamenow,query,temp)
        filenamenow,temp = temp,filenamenow
    filterdata(filenamenow,outputfilename)

filename = r"C:\Users\goela\Development\Python\myfile.txt"
outputfilename = r"C:\Users\goela\Development\Python\myoutputfile.txt"
query = 'IGEM Competition'
info(filename,query,outputfilename)
