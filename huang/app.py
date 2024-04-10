from flask import Flask, render_template, redirect, url_for, request, session,flash
import mysql.connector
from flask import send_from_directory

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL connection settings
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'yonghu'
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# ... (其他代码)

#主界面
@app.route('/index')
def index():
    if 'username' in session:
        return render_template('dzlhuanghe/index.html')
    else:
        return render_template('login.html')

@app.route('/huanghexuanyan')
def huanghexuanyan():
    if 'username' in session:
        return render_template('dzlhuanghe/index.html')
    else:
        return render_template('login.html')
        
@app.route('/huanghewenhualuntan')
def huanghewenhualuntan():
    if 'username' in session:
        return render_template('dzlhuanghe/index.html')
    else:
        return render_template('login.html')
        
        
@app.route('/huanghewenhualuncong')
def huanghewenhualuncong():
    if 'username' in session:
        return render_template('dzlhuanghe/index.html')
    else:
        return render_template('login.html')
        
        
@app.route('/huanghewenhuaxueyanjiu')
def huanghewenhuaxueyanjiu():
    if 'username' in session:
        return render_template('dzlhuanghe/index.html')
    else:
        return render_template('login.html')
        
           
@app.route('/huanghefeiyi')
def huanghefeiyi():
    if 'username' in session:
        return render_template('dzlhuanghe/index.html')
    else:
        return render_template('login.html')
          
@app.route('/huangheguojiawenhuagongyuan')
def huangheguojiawenhuagongyuan():
    if 'username' in session:
        return render_template('dzlhuanghe/index.html')
    else:
        return render_template('login.html')
        
        
@app.route('/huanghewenhuashuzihua')
def huanghewenhuashuzihua():
    if 'username' in session:
        return render_template('dzlhuanghe/index.html')
    else:
        return render_template('login.html')
                
@app.route('/huanghewenyi')
def huanghewenyi():
    if 'username' in session:
        return render_template('dzlhuanghe/index.html')
    else:
        return render_template('login.html')
        
        
@app.route('/huangheshuhua')
def huangheshuhua():
    if 'username' in session:
        return render_template('dzlhuanghe/index.html')
    else:
        return render_template('login.html')
        
        
@app.route('/huangherenwu')
def huangherenwu():
    if 'username' in session:
        return render_template('dzlhuanghe/index.html')
    else:
        return render_template('login.html')
        
        
@app.route('/huangheshici')
def huangheshici():
    if 'username' in session:
        return render_template('dzlhuanghe/index.html')
    else:
        return render_template('login.html')
          
@app.route('/huanghewenhuajiaoliu')
def huanghewenhuajiaoliu():
    if 'username' in session:
        return render_template('dzlhuanghe/index.html')
    else:
        return render_template('login.html')
        





@app.route('/112')
def h112():
    if 'username' in session:
        return render_template('dzlhuanghe/112.html')
    else:
        return render_template('login.html')

@app.route('/119')
def h119():
    if 'username' in session:
        return render_template('dzlhuanghe/119.html')
    else:
        return render_template('login.html')
@app.route('/120')
def h120():
    if 'username' in session:
        return render_template('dzlhuanghe/120.html')
    else:
        return render_template('login.html')

@app.route('/121')
def h121():
    if 'username' in session:
        return render_template('dzlhuanghe/121.html')
    else:
        return render_template('login.html')


@app.route('/124')
def h124():
    if 'username' in session:
        return render_template('dzlhuanghe/124.html')
    else:
        return render_template('login.html')
@app.route('/125')
def h125():
    if 'username' in session:
        return render_template('dzlhuanghe/125.html')
    else:
        return render_template('login.html')

@app.route('/126')
def h126():
    if 'username' in session:
        return render_template('dzlhuanghe/126.html')
    else:
        return render_template('login.html')

@app.route('/128')
def h128():
    if 'username' in session:
        return render_template('dzlhuanghe/128.html')
    else:
        return render_template('login.html')

@app.route('/130')
def h130():
    if 'username' in session:
        return render_template('dzlhuanghe/130.html')
    else:
        return render_template('login.html')


@app.route('/132')
def h132():
    if 'username' in session:
        return render_template('dzlhuanghe/132.html')
    else:
        return render_template('login.html')

@app.route('/133')
def h133():
    if 'username' in session:
        return render_template('dzlhuanghe/133.html')
    else:
        return render_template('login.html')


@app.route('/134')
def h134():
    if 'username' in session:
        return render_template('dzlhuanghe/134.html')
    else:
        return render_template('login.html')

@app.route('/135')
def h135():
    if 'username' in session:
        return render_template('dzlhuanghe/135.html')
    else:
        return render_template('login.html')

@app.route('/136')
def h136():
    if 'username' in session:
        return render_template('dzlhuanghe/136.html')
    else:
        return render_template('login.html')

@app.route('/137')
def h137():
    if 'username' in session:
        return render_template('dzlhuanghe/137.html')
    else:
        return render_template('login.html')

@app.route('/140')
def h140():
    if 'username' in session:
        return render_template('dzlhuanghe/140.html')
    else:
        return render_template('login.html')

@app.route('/141')
def h141():
    if 'username' in session:
        return render_template('dzlhuanghe/141.html')
    else:
        return render_template('login.html')

@app.route('/142')
def h142():
    if 'username' in session:
        return render_template('dzlhuanghe/142.html')
    else:
        return render_template('login.html')

@app.route('/143')
def h143():
    if 'username' in session:
        return render_template('dzlhuanghe/143.html')
    else:
        return render_template('login.html')

@app.route('/144')
def h144():
    if 'username' in session:
        return render_template('dzlhuanghe/144.html')
    else:
        return render_template('login.html')

@app.route('/145')
def h145():
    if 'username' in session:
        return render_template('dzlhuanghe/145.html')
    else:
        return render_template('login.html')

@app.route('/146')
def h146():
    if 'username' in session:
        return render_template('dzlhuanghe/146.html')
    else:
        return render_template('login.html')

@app.route('/147')
def h147():
    if 'username' in session:
        return render_template('dzlhuanghe/147.html')
    else:
        return render_template('login.html')

@app.route('/148')
def h148():
    if 'username' in session:
        return render_template('dzlhuanghe/148.html')
    else:
        return render_template('login.html')

@app.route('/149')
def h149():
    if 'username' in session:
        return render_template('dzlhuanghe/149.html')
    else:
        return render_template('login.html')

@app.route('/150')
def h150():
    if 'username' in session:
        return render_template('dzlhuanghe/150.html')
    else:
        return render_template('login.html')

@app.route('/151')
def h151():
    if 'username' in session:
        return render_template('dzlhuanghe/151.html')
    else:
        return render_template('login.html')

@app.route('/152')
def h152():
    if 'username' in session:
        return render_template('dzlhuanghe/152.html')
    else:
        return render_template('login.html')

@app.route('/153')
def h153():
    if 'username' in session:
        return render_template('dzlhuanghe/153.html')
    else:
        return render_template('login.html')

@app.route('/154')
def h154():
    if 'username' in session:
        return render_template('dzlhuanghe/154.html')
    else:
        return render_template('login.html')

@app.route('/155')
def h155():
    if 'username' in session:
        return render_template('dzlhuanghe/155.html')
    else:
        return render_template('login.html')

@app.route('/156')
def h156():
    if 'username' in session:
        return render_template('dzlhuanghe/156.html')
    else:
        return render_template('login.html')

@app.route('/157')
def h157():
    if 'username' in session:
        return render_template('dzlhuanghe/157.html')
    else:
        return render_template('login.html')

@app.route('/158')
def h158():
    if 'username' in session:
        return render_template('dzlhuanghe/158.html')
    else:
        return render_template('login.html')

@app.route('/161')
def h161():
    if 'username' in session:
        return render_template('dzlhuanghe/161.html')
    else:
        return render_template('login.html')

@app.route('/162')
def h162():
    if 'username' in session:
        return render_template('dzlhuanghe/162.html')
    else:
        return render_template('login.html')

@app.route('/163')
def h163():
    if 'username' in session:
        return render_template('dzlhuanghe/163.html')
    else:
        return render_template('login.html')

@app.route('/164')
def h164():
    if 'username' in session:
        return render_template('dzlhuanghe/164.html')
    else:
        return render_template('login.html')

@app.route('/165')
def h165():
    if 'username' in session:
        return render_template('dzlhuanghe/165.html')
    else:
        return render_template('login.html')

@app.route('/166')
def h166():
    if 'username' in session:
        return render_template('dzlhuanghe/166.html')
    else:
        return render_template('login.html')

@app.route('/167')
def h167():
    if 'username' in session:
        return render_template('dzlhuanghe/167.html')
    else:
        return render_template('login.html')

@app.route('/168')
def h168():
    if 'username' in session:
        return render_template('dzlhuanghe/168.html')
    else:
        return render_template('login.html')

@app.route('/169')
def h169():
    if 'username' in session:
        return render_template('dzlhuanghe/169.html')
    else:
        return render_template('login.html')

@app.route('/172')
def h172():
    if 'username' in session:
        return render_template('dzlhuanghe/172.html')
    else:
        return render_template('login.html')

@app.route('/176')
def h176():
    if 'username' in session:
        return render_template('dzlhuanghe/176.html')
    else:
        return render_template('login.html')

@app.route('/177')
def h177():
    if 'username' in session:
        return render_template('dzlhuanghe/177.html')
    else:
        return render_template('login.html')

@app.route('/178')
def h178():
    if 'username' in session:
        return render_template('dzlhuanghe/178.html')
    else:
        return render_template('login.html')

@app.route('/179')
def h179():
    if 'username' in session:
        return render_template('dzlhuanghe/179.html')
    else:
        return render_template('login.html')

@app.route('/180')
def h180():
    if 'username' in session:
        return render_template('dzlhuanghe/180.html')
    else:
        return render_template('login.html')

@app.route('/181')
def h181():
    if 'username' in session:
        return render_template('dzlhuanghe/181.html')
    else:
        return render_template('login.html')

@app.route('/182')
def h182():
    if 'username' in session:
        return render_template('dzlhuanghe/182.html')
    else:
        return render_template('login.html')

@app.route('/183')
def h183():
    if 'username' in session:
        return render_template('dzlhuanghe/183.html')
    else:
        return render_template('login.html')

@app.route('/184')
def h184():
    if 'username' in session:
        return render_template('dzlhuanghe/184.html')
    else:
        return render_template('login.html')

@app.route('/185')
def h185():
    if 'username' in session:
        return render_template('dzlhuanghe/185.html')
    else:
        return render_template('login.html')

@app.route('/186')
def h186():
    if 'username' in session:
        return render_template('dzlhuanghe/186.html')
    else:
        return render_template('login.html')

@app.route('/187')
def h187():
    if 'username' in session:
        return render_template('dzlhuanghe/187.html')
    else:
        return render_template('login.html')

@app.route('/188')
def h188():
    if 'username' in session:
        return render_template('dzlhuanghe/188.html')
    else:
        return render_template('login.html')

@app.route('/189')
def h189():
    if 'username' in session:
        return render_template('dzlhuanghe/189.html')
    else:
        return render_template('login.html')

@app.route('/190')
def h190():
    if 'username' in session:
        return render_template('dzlhuanghe/190.html')
    else:
        return render_template('login.html')

@app.route('/191')
def h191():
    if 'username' in session:
        return render_template('dzlhuanghe/191.html')
    else:
        return render_template('login.html')

@app.route('/192')
def h192():
    if 'username' in session:
        return render_template('dzlhuanghe/192.html')
    else:
        return render_template('login.html')

@app.route('/193')
def h193():
    if 'username' in session:
        return render_template('dzlhuanghe/193.html')
    else:
        return render_template('login.html')

@app.route('/194')
def h194():
    if 'username' in session:
        return render_template('dzlhuanghe/194.html')
    else:
        return render_template('login.html')

@app.route('/195')
def h195():
    if 'username' in session:
        return render_template('dzlhuanghe/195.html')
    else:
        return render_template('login.html')

@app.route('/200')
def h200():
    if 'username' in session:
        return render_template('dzlhuanghe/200.html')
    else:
        return render_template('login.html')

@app.route('/201')
def h201():
    if 'username' in session:
        return render_template('dzlhuanghe/201.html')
    else:
        return render_template('login.html')

@app.route('/204')
def h204():
    if 'username' in session:
        return render_template('dzlhuanghe/204.html')
    else:
        return render_template('login.html')

@app.route('/206')
def h206():
    if 'username' in session:
        return render_template('dzlhuanghe/206.html')
    else:
        return render_template('login.html')

@app.route('/208')
def h208():
    if 'username' in session:
        return render_template('dzlhuanghe/208.html')
    else:
        return render_template('login.html')

@app.route('/209')
def h209():
    if 'username' in session:
        return render_template('dzlhuanghe/209.html')
    else:
        return render_template('login.html')

@app.route('/210')
def h210():
    if 'username' in session:
        return render_template('dzlhuanghe/210.html')
    else:
        return render_template('login.html')

@app.route('/211')
def h211():
    if 'username' in session:
        return render_template('dzlhuanghe/211.html')
    else:
        return render_template('login.html')

@app.route('/219')
def h219():
    if 'username' in session:
        return render_template('dzlhuanghe/219.html')
    else:
        return render_template('login.html')

@app.route('/220')
def h220():
    if 'username' in session:
        return render_template('dzlhuanghe/220.html')
    else:
        return render_template('login.html')

@app.route('/222')
def h222():
    if 'username' in session:
        return render_template('dzlhuanghe/222.html')
    else:
        return render_template('login.html')

@app.route('/225')
def h225():
    if 'username' in session:
        return render_template('dzlhuanghe/225.html')
    else:
        return render_template('login.html')

@app.route('/226')
def h226():
    if 'username' in session:
        return render_template('dzlhuanghe/226.html')
    else:
        return render_template('login.html')

@app.route('/227')
def h227():
    if 'username' in session:
        return render_template('dzlhuanghe/227.html')
    else:
        return render_template('login.html')

@app.route('/231')
def h231():
    if 'username' in session:
        return render_template('dzlhuanghe/231.html')
    else:
        return render_template('login.html')

@app.route('/237')
def h237():
    if 'username' in session:
        return render_template('dzlhuanghe/237.html')
    else:
        return render_template('login.html')

@app.route('/256')
def h256():
    if 'username' in session:
        return render_template('dzlhuanghe/256.html')
    else:
        return render_template('login.html')

@app.route('/257')
def h257():
    if 'username' in session:
        return render_template('dzlhuanghe/257.html')
    else:
        return render_template('login.html')

@app.route('/258')
def h258():
    if 'username' in session:
        return render_template('dzlhuanghe/258.html')
    else:
        return render_template('login.html')

@app.route('/259')
def h259():
    if 'username' in session:
        return render_template('dzlhuanghe/259.html')
    else:
        return render_template('login.html')

@app.route('/260')
def h260():
    if 'username' in session:
        return render_template('dzlhuanghe/260.html')
    else:
        return render_template('login.html')

@app.route('/263')
def h263():
    if 'username' in session:
        return render_template('dzlhuanghe/263.html')
    else:
        return render_template('login.html')

@app.route('/264')
def h264():
    if 'username' in session:
        return render_template('dzlhuanghe/264.html')
    else:
        return render_template('login.html')

@app.route('/265')
def h265():
    if 'username' in session:
        return render_template('dzlhuanghe/265.html')
    else:
        return render_template('login.html')

@app.route('/268')
def h268():
    if 'username' in session:
        return render_template('dzlhuanghe/268.html')
    else:
        return render_template('login.html')

@app.route('/276')
def h276():
    if 'username' in session:
        return render_template('dzlhuanghe/276.html')
    else:
        return render_template('login.html')

@app.route('/277')
def h277():
    if 'username' in session:
        return render_template('dzlhuanghe/277.html')
    else:
        return render_template('login.html')

@app.route('/278')
def h278():
    if 'username' in session:
        return render_template('dzlhuanghe/278.html')
    else:
        return render_template('login.html')

@app.route('/guanggaofuwu')
def guanggaofuwu():
    if 'username' in session:
        return render_template('dzlhuanghe/guanggaofuwu.html')
    else:
        return render_template('login.html')

@app.route('/guanyubenwang')
def guanyubenwang():
    if 'username' in session:
        return render_template('dzlhuanghe/guanyubenwang.html')
    else:
        return render_template('login.html')
  
@app.route('/huanghejingji')
def huanghejingji():
    if 'username' in session:
        return render_template('dzlhuanghe/huanghejingji.html')
    else:
        return render_template('login.html')
  
@app.route('/huanghelvyou')
def huanghelvyou():
    if 'username' in session:
        return render_template('dzlhuanghe/huanghelvyou.html')
    else:
        return render_template('login.html')
  
@app.route('/huanghemeishi')
def huanghemeishi():
    if 'username' in session:
        return render_template('dzlhuanghe/huanghemeishi.html')
    else:
        return render_template('login.html')
  
@app.route('/huanghemeitu')
def huanghemeitu():
    if 'username' in session:
        return render_template('dzlhuanghe/huanghemeitu.html')
    else:
        return render_template('login.html')
  
@app.route('/huanghewenhua')
def huanghewenhua():
    if 'username' in session:
        return render_template('dzlhuanghe/huanghewenhua.html')
    else:
        return render_template('login.html')
  
@app.route('/huanghexinwen')
def huanghexinwen():
    if 'username' in session:
        return render_template('dzlhuanghe/huanghexinwen.html')
    else:
        return render_template('login.html')
  
@app.route('/huangyanhuichengyuan')
def huangyanhuichengyuan():
    if 'username' in session:
        return render_template('dzlhuanghe/huangyanhuichengyuan.html')
    else:
        return render_template('login.html')
  
@app.route('/huangyanhuigaikuang')
def huangyanhuigaikuang():
    if 'username' in session:
        return render_template('dzlhuanghe/huangyanhuigaikuang.html')
    else:
        return render_template('login.html')
  
@app.route('/jiankangwenhua')
def jiankangwenhua():
    if 'username' in session:
        return render_template('dzlhuanghe/jiankangwenhua.html')
    else:
        return render_template('login.html')
  
@app.route('/kejijiaoyu')
def kejijiaoyu():
    if 'username' in session:
        return render_template('dzlhuanghe/kejijiaoyu.html')
    else:
        return render_template('login.html')
  
@app.route('/lianxiwomen')
def lianxiwomen():
    if 'username' in session:
        return render_template('dzlhuanghe/lianxiwomen.html')
    else:
        return render_template('login.html')
  
@app.route('/minsujieqing')
def minsujieqing():
    if 'username' in session:
        return render_template('dzlhuanghe/minsujieqing.html')
    else:
        return render_template('login.html')
  
@app.route('/qitashengquhuangyancuhuixinwen')
def qitashengquhuangyancuhuixinwen():
    if 'username' in session:
        return render_template('dzlhuanghe/qitashengquhuangyancuhuixinwen.html')
    else:
        return render_template('login.html')
  
@app.route('/shanxihuangyanhuixinwen')
def shanxihuangyanhuixinwen():
    if 'username' in session:
        return render_template('dzlhuanghe/shanxihuangyanhuixinwen.html')
    else:
        return render_template('login.html')
  
@app.route('/shengtaihuanbao')
def shengtaihuanbao():
    if 'username' in session:
        return render_template('dzlhuanghe/shengtaihuanbao.html')
    else:
        return render_template('login.html')
  
@app.route('/xiandaihuayanjiu')
def xiandaihuayanjiu():
    if 'username' in session:
        return render_template('dzlhuanghe/xiandaihuayanjiu.html')
    else:
        return render_template('login.html')
  
@app.route('/xinwendongtai-desc_2')
def xinwendongtai_desc_2():
    if 'username' in session:
        return render_template('dzlhuanghe/xinwendongtai-desc_2.html')
    else:
        return render_template('login.html')
  
@app.route('/xinwendongtai-desc_3')
def xinwendongtai_desc_3():
    if 'username' in session:
        return render_template('dzlhuanghe/xinwendongtai-desc_3.html')
    else:
        return render_template('login.html')
  
@app.route('/xinwendongtai-desc_4')
def xinwendongtai_desc_4():
    if 'username' in session:
        return render_template('dzlhuanghe/xinwendongtai-desc_4.html')
    else:
        return render_template('login.html')
  
@app.route('/xinwendongtai')
def xinwendongtai():
    if 'username' in session:
        return render_template('dzlhuanghe/xinwendongtai.html')
    else:
        return render_template('login.html')
    
@app.route('/huangheshipin')
def huangheshipin():
    if 'username' in session:
        return render_template('dzlhuanghe/huangheshipin.html')
    else:
        return render_template('login.html')
  
@app.route('/yanjiuhuizhangcheng')
def yanjiuhuizhangcheng():
    if 'username' in session:
        return render_template('dzlhuanghe/yanjiuhuizhangcheng.html')
    else:
        return render_template('login.html')
  
@app.route('/zuzhijiegou')
def zuzhijiegou():
    if 'username' in session:
        return render_template('dzlhuanghe/zuzhijiegou.html')
    else:
        return render_template('login.html')
  

@app.route('/liuyan', methods=['POST'])  
def liuyan():
    if 'username' in session:
        return render_template('liuyan.html')
    else:
        return render_template('login.html')  






#登录
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = query_user(username, password)
        if user and username == 'admin':
            session['username'] = username
            return redirect(url_for('user_management'))
        elif user:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = '用户名或密码错误'
            

    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    # ... (处理注册逻辑)
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            error = '两次输入的密码不一致'
        elif len(username) < 3 or len(password) < 6:
            error = '用户名至少3位，密码至少6位'
        elif query_user(username, password):
            error = '用户名已存在'
        else:
            # 连接数据库并插入新用户
            cursor.execute("INSERT INTO hh_user (userName, pwd) VALUES (%s, %s)", (username, password))
            cnx.commit()
            flash('注册成功，请登录！', 'success')
            return redirect(url_for('login'))

    return render_template('register.html', error=error)
#注销
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

#用户管理
@app.route('/admin/user_management')
def user_management():
    cursor.execute("SELECT * FROM hh_user")
    users = cursor.fetchall()

    # 将查询结果转换为字典列表
    users = [dict(zip([column[0] for column in cursor.description], row)) for row in users]
    
    return render_template('admin/user_management.html', users=users)

#添加用户
@app.route('/admin/user/add', methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    
    # 验证用户名和密码是否符合要求，以及是否已存在
    existing_user = check_if_username_exists(username)
    if existing_user:
        flash('用户名已存在', 'danger')
        return redirect(url_for('user_management'))
    elif len(username) < 3 or len(password) < 6:
        flash('用户名至少3位，密码至少6位', 'danger')
        return redirect(url_for('user_management'))

    # 连接数据库并插入新用户
    cursor.execute("INSERT INTO hh_user (userName, pwd) VALUES (%s, %s)", (username, password))
    cnx.commit()  # 如果使用连接池，可能需要调用不同的方法提交事务
    flash('用户添加成功！', 'success')
    return redirect(url_for('user_management'))

#修改用户信息
@app.route('/admin/user/<int:user_id>/edit', methods=['POST'])
def edit_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        flash('用户不存在', 'danger')
        return redirect(url_for('user_management'))

    new_username = request.form['username']
    new_password = request.form['password']

    # 验证用户名和密码是否符合要求，以及是否已存在（排除当前用户）
    existing_user = check_if_username_exists(new_username, exclude_id=user_id)
    if existing_user:
        flash('用户名已存在', 'danger')
        return redirect(url_for('user_management'))
    elif len(new_username) < 3 and new_password:
        flash('用户名至少3位，密码至少6位', 'danger')
        return redirect(url_for('user_management'))

    # 连接数据库并更新用户信息
    cursor.execute(
        "UPDATE hh_user SET userName = %s, pwd = %s WHERE id = %s",
        (new_username, new_password or user.pwd, user_id)
    )
    cnx.commit()  # 如果使用连接池，可能需要调用不同的方法提交事务
    flash('用户信息已更新！', 'success')
    return redirect(url_for('user_management'))
     
#删除用户信息
@app.route('/admin/user/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        flash('用户不存在', 'danger')
        return redirect(url_for('user_management'))

    cursor.execute("DELETE FROM hh_user WHERE id = %s", (user_id,))
    cnx.commit()  # 如果使用连接池，可能需要调用不同的方法提交事务
    flash('用户已删除！', 'success')
    return redirect(url_for('user_management'))

def check_if_username_exists(username, exclude_id=None):
    query = "SELECT COUNT(*) FROM hh_user WHERE userName = %s"
    params = (username,)
    
    if exclude_id is not None:
        query += " AND id != %s"
        params += (exclude_id,)

    cursor.execute(query, params)
    count = cursor.fetchone()[0]
    return count > 0

def get_user_by_id(user_id):
    cursor.execute("SELECT * FROM hh_user WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    if user:
        return dict(zip([column[0] for column in cursor.description], user))
    return None
#通过账号密码查询用户是否存在
def query_user(username, password):
    cursor.execute("SELECT * FROM hh_user WHERE userName = %s AND pwd = %s", (username, password))
    result = cursor.fetchone()
    return result


if __name__ == '__main__':
    app.run(debug=True)