from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
from sqlalchemy import and_


app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///class.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
app.config['SQLALCHEMY_ECHO']=True

db = SQLAlchemy(app)
url = 'http://127.0.0.1:5000/'
al = ['A','B','C','D','E','F','G']
day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
time = [1, 2, 3, 4, 5]

# 講義の時間
start_default = [0,"9:00","10:50","13:20","15:10","17:00","18:50"]
end_default = [0,"10:40","12:30","15:00","16:50","18:40","20:30"]

# 曜日、時間、講義名、講義形態、講師名、教材、教室、ZoomURL、ZoomID、ZoomPassを設定
class ClassArticle(db.Model):
    day = db.Column(db.String(20), nullable=False)
    time = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=True, default=" ")
    type = db.Column(db.String(8), nullable=True)
    teacher = db.Column(db.String(10), nullable=True)
    file_url = db.Column(db.String(1000), nullable=True)
    classroom = db.Column(db.String(10), nullable=True)
    zoom_url = db.Column(db.String(1000), nullable=True)
    zoom_id = db.Column(db.String(11), nullable=True)
    zoom_pass = db.Column(db.String(30), nullable=True)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

# 初めてのアクセス時にデータベースを作成する。
@app.before_first_request
def init():
    db.create_all()
    for i in range(5):
        classarticle = ClassArticle(day=day[0], time=time[i], name=None, type=None,
                                    teacher=None,
                                    file_url=None, classroom=None,
                                    zoom_url=None, zoom_id=None, zoom_pass=None)
        db.session.add(classarticle)

    for i in range(5):
        classarticle = ClassArticle(day=day[1], time=time[i], name=None, type=None,
                                    teacher=None,
                                    file_url=None, classroom=None,
                                    zoom_url=None, zoom_id=None, zoom_pass=None)
        db.session.add(classarticle)

    for i in range(5):
        classarticle = ClassArticle(day=day[2], time=time[i], name=None, type=None,
                                    teacher=None,
                                    file_url=None, classroom=None,
                                    zoom_url=None, zoom_id=None, zoom_pass=None)
        db.session.add(classarticle)

    for i in range(5):
        classarticle = ClassArticle(day=day[3], time=time[i], name=None, type=None,
                                    teacher=None,
                                    file_url=None, classroom=None,
                                    zoom_url=None, zoom_id=None, zoom_pass=None)
        db.session.add(classarticle)

    for i in range(5):
        classarticle = ClassArticle(day=day[4], time=time[i], name=None, type=None,
                                    teacher=None,
                                    file_url=None, classroom=None,
                                    zoom_url=None, zoom_id=None, zoom_pass=None)
        db.session.add(classarticle)

    for i in range(5):
        classarticle = ClassArticle(day=day[5], time=time[i], name=None, type=None,
                                    teacher=None,
                                    file_url=None, classroom=None,
                                    zoom_url=None, zoom_id=None, zoom_pass=None)
        db.session.add(classarticle)

    db.session.commit()

# /はホームページ
@app.route('/')
def index():
    if request.method == 'GET':
        classarticles = ClassArticle.query
        ones = classarticles.filter(ClassArticle.time==1)
        twos = classarticles.filter(ClassArticle.time==2)
        threes = classarticles.filter(ClassArticle.time==3)
        fours = classarticles.filter(ClassArticle.time==4)
        fives = classarticles.filter(ClassArticle.time==5)
        sixs = classarticles.filter(ClassArticle.time==6)
        dt_now = dt.now()
        day = dt_now.strftime('%A')
        today = classarticles.filter(ClassArticle.day==day)
        return render_template('index.html',title='hoseiZoom',day=day,ones=ones,twos=twos,threes=threes,fours=fours,fives=fives,sixs=sixs,today=today
                                    ,start_default=start_default,end_default=end_default)

# /setting1は個人の講義スケジュールを設定。
@app.route('/setting1', methods=['GET','POST'])
def setting1():
    if request.method == 'POST':

        
        #　月曜の時間割
        name_mon = []
        type_mon = []
        teacher_mon = []
        file_url_mon = []
        classroom_mon = []
        zoom_url_mon = []
        zoom_id_mon = []
        zoom_pass_mon = []
        
        for i in range(1,6):
            name = request.form.get(f'name_mon{i}')
            if name == None:
                name = " "
            type = request.form.get(f'type_mon{i}')
            if type == None:
                type = " "
            teacher = request.form.get(f'teacher_mon{i}')
            if teacher == None:
                teacher = " "
            file_url = request.form.get(f'file_url_mon{i}')
            if file_url == None:
                file_url = " "
            classroom = request.form.get(f'classroom_mon{i}')
            if classroom == None:
                classroom = " "
            zoom_url = request.form.get(f'zoom_url_mon{i}')
            if zoom_url == None:
                zoom_url = " "
            zoom_id = request.form.get(f'zoom_id_mon{i}')
            if zoom_id == None:
                zoom_id = " "
            zoom_pass = request.form.get(f'zoom_pass_mon{i}')
            if zoom_pass == None:
                zoom_pass = " "
            
            name_mon.append(name)
            type_mon.append(type)
            teacher_mon.append(teacher)
            file_url_mon.append(file_url)
            classroom_mon.append(classroom)
            zoom_url_mon.append(zoom_url)
            zoom_id_mon.append(zoom_id)
            zoom_pass_mon.append(zoom_pass)
        
        #　火曜の時間割
        name_tue = []
        type_tue = []
        teacher_tue = []
        file_url_tue = []
        classroom_tue = []
        zoom_url_tue = []
        zoom_id_tue = []
        zoom_pass_tue = []
        for i in range(1, 6):


            name = request.form.get(f'name_tue{i}')
            if name == None:
                name = " "
            type = request.form.get(f'type_tue{i}')
            if type == None:
                type = " "
            teacher = request.form.get(f'teacher_tue{i}')
            if teacher == None:
                teacher = " "
            file_url = request.form.get(f'file_url_tue{i}')
            if file_url == None:
                file_url = " "
            classroom = request.form.get(f'classroom_tue{i}')
            if classroom == None:
                classroom = " "
            zoom_url = request.form.get(f'zoom_url_tue{i}')
            if zoom_url == None:
                zoom_url = " "
            zoom_id = request.form.get(f'zoom_id_tue{i}')
            if zoom_id == None:
                zoom_id = " "
            zoom_pass = request.form.get(f'zoom_pass_tue{i}')
            if zoom_pass == None:
                zoom_pass = " "
            

            name_tue.append(name)
            type_tue.append(type)
            teacher_tue.append(teacher)
            file_url_tue.append(file_url)
            classroom_tue.append(classroom)
            zoom_url_tue.append(zoom_url)
            zoom_id_tue.append(zoom_id)
            zoom_pass_tue.append(zoom_pass)
            
        #　水曜の時間割
        name_wed = []
        type_wed = []
        teacher_wed = []
        file_url_wed = []
        classroom_wed = []
        zoom_url_wed = []
        zoom_id_wed = []
        zoom_pass_wed = []
        
        for i in range(1, 6):
            
            name = request.form.get(f'name_wed{i}')
            if name == None:
                name = " "
            type = request.form.get(f'type_wed{i}')
            if type == None:
                type = " "
            teacher = request.form.get(f'teacher_wed{i}')
            if teacher == None:
                teacher = " "
            file_url = request.form.get(f'file_url_wed{i}')
            if file_url == None:
                file_url = " "
            classroom = request.form.get(f'classroom_wed{i}')
            if classroom == None:
                classroom = " "
            zoom_url = request.form.get(f'zoom_url_wed{i}')
            if zoom_url == None:
                zoom_url = " "
            zoom_id = request.form.get(f'zoom_id_wed{i}')
            if zoom_id == None:
                zoom_id = " "
            zoom_pass = request.form.get(f'zoom_pass_wed{i}')
            if zoom_pass == None:
                zoom_pass = " "
            

            name_wed.append(name)
            type_wed.append(type)
            teacher_wed.append(teacher)
            file_url_wed.append(file_url)
            classroom_wed.append(classroom)
            zoom_url_wed.append(zoom_url)
            zoom_id_wed.append(zoom_id)
            zoom_pass_wed.append(zoom_pass)

        #　木曜の時間割
        name_thu = []
        type_thu = []
        teacher_thu = []
        file_url_thu = []
        classroom_thu = []
        zoom_url_thu = []
        zoom_id_thu = []
        zoom_pass_thu = []
        
        for i in range(1, 6):

            name = request.form.get(f'name_thu{i}')
            if name == None:
                name = " "
            type = request.form.get(f'type_thu{i}')
            if type == None:
                type = " "
            teacher = request.form.get(f'teacher_thu{i}')
            if teacher == None:
                teacher = " "
            file_url = request.form.get(f'file_url_thu{i}')
            if file_url == None:
                file_url = " "
            classroom = request.form.get(f'classroom_thu{i}')
            if classroom == None:
                classroom = " "
            zoom_url = request.form.get(f'zoom_url_thu{i}')
            if zoom_url == None:
                zoom_url = " "
            zoom_id = request.form.get(f'zoom_id_thu{i}')
            if zoom_id == None:
                zoom_id = " "
            zoom_pass = request.form.get(f'zoom_pass_thu{i}')
            if zoom_pass == None:
                zoom_pass = " "
            

            name_thu.append(name)
            type_thu.append(type)
            teacher_thu.append(teacher)
            file_url_thu.append(file_url)
            classroom_thu.append(classroom)
            zoom_url_thu.append(zoom_url)
            zoom_id_thu.append(zoom_id)
            zoom_pass_thu.append(zoom_pass)

        #　金曜の時間割
        name_fri = []
        type_fri = []
        teacher_fri = []
        file_url_fri = []
        classroom_fri = []
        zoom_url_fri = []
        zoom_id_fri = []
        zoom_pass_fri = []
        for i in range(1, 6):
            
            name = request.form.get(f'name_fri{i}')
            if name == None:
                name = " "
            type = request.form.get(f'type_fri{i}')
            if type == None:
                type = " "
            teacher = request.form.get(f'teacher_fri{i}')
            if teacher == None:
                teacher = " "
            file_url = request.form.get(f'file_url_fri{i}')
            if file_url == None:
                file_url = " "
            classroom = request.form.get(f'classroom_fri{i}')
            if classroom == None:
                classroom = " "
            zoom_url = request.form.get(f'zoom_url_fri{i}')
            if zoom_url == None:
                zoom_url = " "
            zoom_id = request.form.get(f'zoom_id_fri{i}')
            if zoom_id == None:
                zoom_id = " "
            zoom_pass = request.form.get(f'zoom_pass_fri{i}')
            if zoom_pass == None:
                zoom_pass = " "
            

            name_fri.append(name)
            type_fri.append(type)
            teacher_fri.append(teacher)
            file_url_fri.append(file_url)
            classroom_fri.append(classroom)
            zoom_url_fri.append(zoom_url)
            zoom_id_fri.append(zoom_id)
            zoom_pass_fri.append(zoom_pass)

        #　土曜の時間割
        name_sat = []
        type_sat = []
        teacher_sat = []
        file_url_sat = []
        classroom_sat = []
        zoom_url_sat = []
        zoom_id_sat = []
        zoom_pass_sat = []        
        for i in range(1, 6):

            name = request.form.get(f'name_sat{i}')
            if name == None:
                name = " "
            type = request.form.get(f'type_sat{i}')
            if type == None:
                type = " "
            teacher = request.form.get(f'teacher_sat{i}')
            if teacher == None:
                teacher = " "
            file_url = request.form.get(f'file_url_sat{i}')
            if file_url == None:
                file_url = " "
            classroom = request.form.get(f'classroom_sat{i}')
            if classroom == None:
                classroom = " "
            zoom_url = request.form.get(f'zoom_url_sat{i}')
            if zoom_url == None:
                zoom_url = " "
            zoom_id = request.form.get(f'zoom_id_sat{i}')
            if zoom_id == None:
                zoom_id = " "
            zoom_pass = request.form.get(f'zoom_pass_sat{i}')
            if zoom_pass == None:
                zoom_pass = " "
            

            name_sat.append(name)
            type_sat.append(type)
            teacher_sat.append(teacher)
            file_url_sat.append(file_url)
            classroom_sat.append(classroom)
            zoom_url_sat.append(zoom_url)
            zoom_id_sat.append(zoom_id)
            zoom_pass_sat.append(zoom_pass)


######入力した情報をデータベースに反映#######################################################################################################
        name_list = [name_mon, name_tue, name_wed, name_thu, name_fri, name_sat]
        type_list = [type_mon, type_tue, type_wed, type_thu, type_fri, type_sat]
        teacher_list = [teacher_mon, teacher_tue, teacher_wed, teacher_thu, teacher_fri, teacher_sat]
        file_url_list = [file_url_mon, file_url_tue, file_url_wed, file_url_thu, file_url_fri, file_url_sat]
        classroom_list = [classroom_mon, classroom_tue, classroom_wed, classroom_thu, classroom_fri, classroom_sat]
        zoom_url_list = [zoom_url_mon, zoom_url_tue, zoom_url_wed, zoom_url_thu, zoom_url_fri, zoom_url_sat]
        zoom_id_list = [zoom_id_mon, zoom_id_tue, zoom_id_wed, zoom_id_thu, zoom_id_fri, zoom_id_sat]
        zoom_pass_list = [zoom_pass_mon, zoom_pass_tue, zoom_pass_wed, zoom_pass_thu, zoom_pass_fri, zoom_pass_sat]
        
        for i in range(6):
            name = name_list[i]
            type = type_list[i]
            teacher = teacher_list[i]
            file_url = file_url_list[i]
            classroom = classroom_list[i]
            zoom_url = zoom_url_list[i]
            zoom_id = zoom_id_list[i]
            zoom_pass = zoom_pass_list[i]

            for k in range(5):
                id = str(i*5 + k + 1)
                a = ClassArticle.query.get(id)
                a.name = name[k]
                a.type = type[k]
                a.teacher = teacher[k]
                a.file_url = file_url[k]
                a.classroom = classroom[k]
                a.zoom_url = zoom_url[k]
                a.zoom_id = zoom_id[k]
                a.zoom_pass = zoom_pass[k]

        db.session.commit()
        """       
        for i in range(5):
            d = db.session.filter(and_(ClassArticle.day==day[0], ClassArticle.time == time[i]))
            print(d.day())
            d.name = name_mon[i]
            d.type = type_mon[i]
            d.teacher = teacher_mon[i]
            d.file_url = file_url_mon[i]
            d.classroom = classroom_mon[i]
            d.zoom_url = zoom_url_mon[i]
            d.zoom_id = zoom_id_mon[i]
            d.zoom_pass = zoom_pass_mon[i]
            print(d.name)
            
            d.commit()
            
            classarticle = ClassArticle(day=day[0], time=time[i], name=name_mon[i], type=type_mon[i], teacher=teacher_mon[i],
                                        file_url=file_url_mon[i], classroom=classroom_mon[i],
                                        zoom_url=zoom_url_mon[i], zoom_id=zoom_id_mon[i], zoom_pass=zoom_pass_mon[i])
            
            db.session.add(classarticle)
            

        for i in range(5):
            d = db.session.filter(and_(ClassArticle.day == day[1], ClassArticle.time == time[i])).first()
            d.name = name_tue[i]
            d.type = type_tue[i]
            d.teacher = teacher_tue[i]
            d.file_url = file_url_tue[i]
            d.classroom = classroom_tue[i]
            d.zoom_url = zoom_url_tue[i]
            d.zoom_id = zoom_id_tue[i]
            d.zoom_pass = zoom_pass_tue[i]
            print(d.name)
            
            d.commit()

            
            classarticle = ClassArticle(day=day[1], time=time[i], name=name_tue[i], type=type_tue[i], teacher=teacher_tue[i],
                                        file_url=file_url_tue[i], classroom=classroom_tue[i],
                                        zoom_url=zoom_url_tue[i], zoom_id=zoom_id_tue[i], zoom_pass=zoom_pass_tue[i])
            db.session.add(classarticle)
            

        for i in range(5):
            d = db.session.filter(and_(ClassArticle.day == day[2], ClassArticle.time == time[i])).first()
            d.name = name_wed[i]
            d.type = type_wed[i]
            d.teacher = teacher_wed[i]
            d.file_url = file_url_wed[i]
            d.classroom = classroom_wed[i]
            d.zoom_url = zoom_url_wed[i]
            d.zoom_id = zoom_id_wed[i]
            d.zoom_pass = zoom_pass_wed[i]
            print(d.name)  
            d.commit()          
            
            classarticle = ClassArticle(day=day[2], time=time[i], name=name_wed[i], type=type_wed[i], teacher=teacher_wed[i],
                                        file_url=file_url_wed[i], classroom=classroom_wed[i],
                                        zoom_url=zoom_url_wed[i], zoom_id=zoom_id_wed[i], zoom_pass=zoom_pass_wed[i])
            db.session.add(classarticle)
            
            
        for i in range(5):
            d = db.session.filter(and_(ClassArticle.day == day[3], ClassArticle.time == time[i])).first()
            d.name = name_thu[i]
            d.type = type_thu[i]
            d.teacher = teacher_thu[i]
            d.file_url = file_url_thu[i]
            d.classroom = classroom_thu[i]
            d.zoom_url = zoom_url_thu[i]
            d.zoom_id = zoom_id_thu[i]
            d.zoom_pass = zoom_pass_thu[i]
            print(d.name)    
            d.commit()        
            
            classarticle = ClassArticle(day=day[3], time=time[i], name=name_thu[i], type=type_thu[i], teacher=teacher_thu[i],
                                        file_url=file_url_thu[i], classroom=classroom_thu[i],
                                        zoom_url=zoom_url_thu[i], zoom_id=zoom_id_thu[i], zoom_pass=zoom_pass_thu[i])
            db.session.add(classarticle)
            
            
        for i in range(5):
            d = db.session.filter(and_(ClassArticle.day == day[4], ClassArticle.time == time[i])).first()
            d.name = name_fri[i]
            d.type = type_fri[i]
            d.teacher = teacher_fri[i]
            d.file_url = file_url_fri[i]
            d.classroom = classroom_fri[i]
            d.zoom_url = zoom_url_fri[i]
            d.zoom_id = zoom_id_fri[i]
            d.zoom_pass = zoom_pass_fri[i]
            print(d.name)
            d.commit()            
            
            classarticle = ClassArticle(day=day[3], time=time[i], name=name_fri[i], type=type_fri[i],
                                        teacher=teacher_fri[i],
                                        file_url=file_url_fri[i], classroom=classroom_fri[i],
                                        zoom_url=zoom_url_fri[i], zoom_id=zoom_id_fri[i], zoom_pass=zoom_pass_fri[i])
            db.session.add(classarticle)
            
        for i in range(5):
            d = db.session.filter(and_(ClassArticle.day == day[5], ClassArticle.time == time[i])).first()
            d.name = name_sat[i]
            d.type = type_sat[i]
            d.teacher = teacher_sat[i]
            d.file_url = file_url_sat[i]
            d.classroom = classroom_sat[i]
            d.zoom_url = zoom_url_sat[i]
            d.zoom_id = zoom_id_sat[i]
            d.zoom_pass = zoom_pass_sat[i]
            print(d.name) 
            d.commit()           

            classarticle = ClassArticle(day=day[4], time=time[i], name=name_sat[i], type=type_sat[i], teacher=teacher_sat[i],
                                        file_url=file_url_sat[i], classroom=classroom_sat[i],
                                        zoom_url=zoom_url_sat[i], zoom_id=zoom_id_sat[i], zoom_pass=zoom_pass_sat[i])
            db.session.add(classarticle)
            """
        
        return redirect('/')
    
    else:
        return render_template('setting1.html')
    
######################################################################################################################################


if __name__ == "__main__":
    app.run(debug=True)

