import web
import Image

render = web.template.render('templates/admin/',)

def mkCurDateDir():
    from datetime import date
    import os
    curYear = date.today().year
    curMon = date.today().month
    curDay = date.today().day
    
    uploadDir = 'static/upload'
    if os.path.isdir( uploadDir ):
        newFolderName = uploadDir + '/%d/%d/%d' % ( curYear , curMon , curDay)
        print(newFolderName)
        if os.path.isdir( newFolderName ):
            print(newFolderName," Exists already ")
        else:
            os.makedirs( newFolderName )
            print(newFolderName," Create OK ")
    else:
        print(uploadDir," not exists, script stop ")
    return newFolderName
            
class upload:
            
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return render.upload('')


    def POST(self):
        import time
        x = web.input(myfile={})        
        filedir = "%s" % (mkCurDateDir()) # change this to the directory you want to store the file in.
        
        print (filedir)
        if 'myfile' in x: # to check if the file-object is created
            #filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            #filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            ext = 'jpg'
            filename = '%s.%s' % (time.strftime("%Y%m%d%H%M%S"), ext)
            fout = open(filedir +'/'+ filename,'wb') # creates the file where the uploaded file should be stored
            fout.write(x['upload']) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.

            infile = filedir +'/'+filename
        #    outfile = infile + ".thumbnail"
        #    im = Image.open(filedir +'/'+filename)
        #    im.thumbnail((128, 128))
        #    im.save(outfile, im.format)

        return render.upload(infile)
    


        
        
        