#include <c++/5.4.0/iostream>
#include <c++/5.4.0/sstream>
#include <c++/5.4.0/string>
#include <c++/5.4.0/stdexcept>
#include <c++/5.4.0/vector>
#include <glob.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>


#include <fstream>

#include "recogfile.h"
#include "tts.h"

#include <opencv2/opencv.hpp>
#include <opencv2/dnn.hpp>

#include "viewer.hpp"
#include "APITools.hpp"


#include "ros/ros.h"
#include "std_msgs/String.h"
#include <geometry_msgs/Twist.h>
#include <actionlib/client/simple_action_client.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <tf/transform_datatypes.h>

using namespace cv;
using namespace std;

//int listen_allowed = 0;
int result[5] = {0};
//int wavenum = 0;

//~ void msg_Callback(const std_msgs::String::ConstPtr& msg)
//~ {
    //~ listen_allowed = 1;
//~ }

void txtwrite(string str){
	fstream dataFile;
	dataFile.open("//home//onyxia//catkin_ws//src//sapr//src//result//theSpeechResult.txt", ios::app);
	if(!dataFile){
		cout<<"open src File Error opening"<<endl;
		//return -1;
	}
	
	dataFile<< str <<endl;
}


//--------------------------------------------人群数目及性别检测----------------------------------------- 
string getnum(int num)
{
    switch(num)
    {
        case 0:return "zero";break;
        case 1:return "one";break;
        case 2:return "two";break;
        case 3:return "three";break;
        case 4:return "four";break;
        case 5:return "five";break;
        case 6:return "six";break;
        case 7:return "seven";break;
        case 8:return "eight";break;
        case 9:return "nine";break;
		case 10:return "ten";break;
        default :return "";break;
    }
}

void kinect_detect_face()
{
    std::string ns = K2_DEFAULT_NS;
    std::string topicColor = K2_TOPIC_QHD K2_TOPIC_IMAGE_COLOR K2_TOPIC_IMAGE_RECT;
    std::string topicDepth = K2_TOPIC_QHD K2_TOPIC_IMAGE_DEPTH K2_TOPIC_IMAGE_RECT;
    bool useExact = true;
    bool useCompressed = false;
    Receiver::Mode mode = Receiver::IMAGE;
    topicColor = "/" + ns + topicColor;
    topicDepth = "/" + ns + topicDepth;
    Receiver receiver(topicColor, topicDepth, useExact, useCompressed);
    receiver.start(mode);
    Mat img, depth;
    receiver.imageViewer(img,depth,1);
  
    faceplusplusApi face_dt;

    imshow("former",img);
    if(img.empty()) {cout<<"error";}

		face_dt.facedetect(img, result);
		//wavenum = face_dt.handdetect(img);

    printf("总人数为：%d, 其中男性人数为：%d, 女性人数为：%d\n",result[0],result[1],result[2]);
    imshow("done", img);
    imwrite("//home//onyxia//catkin_ws//src//sapr//src//result//thePersonRecogImg.jpg",img);
    
    string str_all="the total amount of persons is "+getnum(result[0])+" including "+getnum(result[1])+" men and "+getnum(result[2])+" women:";
    tts(str_all.c_str());
    
    txtwrite("the amount statistics: the total amount :"+to_string(result[0])+", the male :"+to_string(result[1])+", the female"+to_string(result[2])+
    ", the person who stand :"+to_string(result[3])+", the person who sit :"+to_string(result[4])+/*", the person who wave arms :"+to_string(wavenum)+*/".");
    waitKey(2);
  
}
/*===========================================================================================================*/




/*===================回答问题========================*/
//bool ques_find_and(std::string str_org, std::initializer_list<std::string> lst) {
	//for (auto i = lst.begin(); i != lst.end();i++) {
		//if (str_org.find(*i) == str_org.npos) {//只要有一个不是就false
			//return false;
		//}
	//}
	//return true;
//}

unsigned int ques_find_or(string str_org, initializer_list<string> lst)
{
	unsigned int find_num = 0;
	for (auto i = lst.begin(); i != lst.end(); i++)
	{
		if (str_org.find(*i) != str_org.npos)
		{
			cout<<*i<<endl;
			return 1;
		}
	}
	return 0;
}

unsigned int find_quest(string quest_str)
{
	if(ques_find_or(quest_str, {"men"})) return 49;
	if(ques_find_or(quest_str, {"women"})) return 50;
    if(ques_find_or(quest_str, {"number"})){if (ques_find_or(quest_str, {"female"})) return 52;  return 51; }
    if(ques_find_or(quest_str, {"people"})){if (ques_find_or(quest_str, {"it"})) return 54; if (ques_find_or(quest_str, {"stand"})) return 53; else return 55;}
    
	if((ques_find_or(quest_str, {"anada"}))&&(ques_find_or(quest_str, {"handsome","person"}))) return 1;
	if((ques_find_or(quest_str, {"anada"}))&&(ques_find_or(quest_str, {"zones","there"}))) return 2;
	if(ques_find_or(quest_str, {"longest"})) return 3;
	if(ques_find_or(quest_str, {"street"})){if (ques_find_or(quest_str, {"longest"})) return 3; else return 4;}
	if(ques_find_or(quest_str, {"bear","cub","exported","ondon"}))  return 5;
	if(ques_find_or(quest_str, {"blackberry","smartphone","develop"})) return 6;
	if(ques_find_or(quest_str, {"largest"})) return 7;
	if((ques_find_or(quest_str, {"anada","invad"}))&&(ques_find_or(quest_str, {"first"}))) return 8;
	if((ques_find_or(quest_str, {"anada","invad"}))&&(ques_find_or(quest_str, {"second"}))) return 9;
	if(ques_find_or(quest_str, {"country","record","gold","medal","lympic"})) return 10;
	if(ques_find_or(quest_str, {"coin","term"})) return 11;
	if((ques_find_or(quest_str, {"anada"}))&&(ques_find_or(quest_str, {"name"}))) return 12;
	if(ques_find_or(quest_str, {"ount", "olice", "formed"})){if(ques_find_or(quest_str, {"oyal", "anadian"})) return 14; else return 13;}
	if(ques_find_or(quest_str, {"r c m p"})) return 15;
	if(ques_find_or(quest_str, {"call"})) return 16;
	if(ques_find_or(quest_str, {"require","build"})){if(ques_find_or(quest_str, {"snow"})) return 18; else return 17;}
	if(ques_find_or(quest_str, {"visit","summer"})) return 19;
	if(ques_find_or(quest_str, {"desert","dessert"})){if(ques_find_or(quest_str, {"big"})) return 21; else return 20;}
	if(ques_find_or(quest_str, {"famous","anadian"})){if(ques_find_or(quest_str, {"female"})) return 23; else return 22;}
	if(ques_find_or(quest_str, {"origin","omic"})) return 24;
	//25 26 nanobot  40 chatbot
	if(ques_find_or(quest_str, {"hard","disk","drive"})) {if (ques_find_or(quest_str, {"com"})) {if (ques_find_or(quest_str, {"when","launch"})) return 28; else return 27;} else return 29;}
	if(ques_find_or(quest_str, {"c a p t h c h a"})) return 30;
	if(ques_find_or(quest_str, {"bug"}))  return 31;
	if(ques_find_or(quest_str, {"mars","Mars"}))  return 32;
	if(ques_find_or(quest_str, {"ndrioid"}))  return 33;
	if(ques_find_or(quest_str, {"chanical"}))  return 34;
	if(ques_find_or(quest_str, {"pass","uring","test"}))  return 35;
	if(ques_find_or(quest_str, {"paradox","state"}))  return 36;
	if(ques_find_or(quest_str, {"knowledge","engineer","bottle","neck"}))  return 37;
	if(ques_find_or(quest_str, {"worr","impact"})) return 38; 
	if(ques_find_or(quest_str, {"threat"}))  return 39;
	if(ques_find_or(quest_str, {"humanity"})){if (ques_find_or(quest_str, {"worr","impact"})) return 39; else return 38;}
	if(ques_find_or(quest_str, {"chat","check"}))  return 40;
	if(ques_find_or(quest_str, {"self","driving","car","safe"}))  return 41;
	if(ques_find_or(quest_str, {"compile"}))  return 42;
	if(ques_find_or(quest_str, {"rogramming","auguage"})){if (ques_find_or(quest_str, {"pa","thon","tern"})) return 44; else return 43;}
	if(ques_find_or(quest_str, {"robot"})) return 45;
	if(ques_find_or(quest_str, {"pple","inventor","micro"})) return 46;
	if(ques_find_or(quest_str, {"consider","programmer"}))  return 47;
	if(ques_find_or(quest_str, {"p d f","file"}))  return 48;
	
	if(ques_find_or(quest_str, {"how","small","can"})) return 26+; else if ((ques_find_or(quest_str, {"what"}))&&(ques_find_or(quest_str, {"is"}))) return 25; else return 0;
    //return 0;
}

//unsigned int find_logic(string quest_str)
//{
	//if(ques_find_or(quest_str, {"no","No","noun","Noun"})) return 0;
	//if(ques_find_or(quest_str, {"yes","Yes","yeah","Yeah"})) return 1;
//}



void answer( int quest_i)
{
	switch (quest_i)
	{
		case 1:tts("Who's the most handsome person in Canada? I know that Justin Trudeau is very handsome."); 
		  txtwrite("Who's the most handsome person in Canada? I know that Justin Trudeau is very handsome.");break;
		case 2:tts("How many time zones are there in Canada? Canada spans almost 10 million square km and comprises 6 time zones");
		  txtwrite("How many time zones are there in Canada? Canada spans almost 10 million square km and comprises 6 time zones"); break;
		case 3:tts("What's the longest street in the world? Yonge Street in Ontario is the longest street in the world.");
		  txtwrite("What's the longest street in the world? Yonge Street in Ontario is the longest street in the world."); break;
		case 4:tts("How long is Yonge Street in Ontario? Yonge street is almost 2,000 km, starting at Lake Ontario, and running north to the Minnesota border."); 
		  txtwrite("How long is Yonge Street in Ontario? Yonge street is almost 2,000 km, starting at Lake Ontario, and running north to the Minnesota border."); break;
		case 5:tts("What's the name of the bear cub exported from Canada to the London Zoo in 1915? The bear cub was named Winnipeg. It inspired the stories of Winnie-the-Pooh."); 
		  txtwrite("What's the name of the bear cub exported from Canada to the London Zoo in 1915? The bear cub was named Winnipeg. It inspired the stories of Winnie-the-Pooh."); break;
		case 6:tts("Where was the Blackberry Smartphone developed? It was developed in Ontario, at Research In Motion's Waterloo offices."); 
		  txtwrite("Where was the Blackberry Smartphone developed? It was developed in Ontario, at Research In Motion's Waterloo offices."); break;
		case 7:tts("What is the world's largest coin? The Big Nickel in Sudbury, Ontario. It is nine meters in diameter."); 
		  txtwrite("What is the world's largest coin? The Big Nickel in Sudbury, Ontario. It is nine meters in diameter."); break;
		case 8:tts("In what year was Canada invaded by the USA for the first time? The first time that the USA invaded Canada was in 1775"); 
		  txtwrite("In what year was Canada invaded by the USA for the first time? The first time that the USA invaded Canada was in 1775");break;
		case 9:tts("What year was Canada invaded by the USA for the second time? The USA invaded Canada a second time in 1812.");
		  txtwrite("What year was Canada invaded by the USA for the second time? The USA invaded Canada a second time in 1812.");break;
		case 10:tts("What country holds the record for the most gold medals at the Winter Olympics? Canada does! With 14 Golds at the 2010 Vancouver Winter Olympics.");
		   txtwrite("What country holds the record for the most gold medals at the Winter Olympics? Canada does! With 14 Golds at the 2010 Vancouver Winter Olympics.");break;
		case 11:tts("Who coined the term Beatlemania? Sandy Gardiner, a journalist of the Ottawa Journal.");
		   txtwrite("Who coined the term Beatlemania? Sandy Gardiner, a journalist of the Ottawa Journal.");break;
		case 12:tts("Why is Canada named Canada? French explorers misunderstood the local native word Kanata, which means village.");
		   txtwrite("Why is Canada named Canada? French explorers misunderstood the local native word Kanata, which means village.");break;
		case 13:tts("When was The Mounted Police formed? The Mounted Police was formed in 1873.");
		   txtwrite("When was The Mounted Police formed? The Mounted Police was formed in 1873.");break;
		case 14:tts("When was The Royal Canadian Mounted Police formed? In 1920, when The Mounted Police merged with the Dominion Police.");
		   txtwrite("When was The Royal Canadian Mounted Police formed? In 1920, when The Mounted Police merged with the Dominion Police.");break;
		case 15:tts("How big is the RCMP? Today, the RCMP has close to 30,000 members.");
		   txtwrite("How big is the RCMP? Today, the RCMP has close to 30,000 members.");break;
		case 16:tts("What else is Montreal called? Montreal is often called the City of Saints or the City of a Hundred Bell Towers.");
		   txtwrite("What else is Montreal called? Montreal is often called the City of Saints or the City of a Hundred Bell Towers.");break;
		case 17:tts("How many tons of ice are required to build The Hotel de Glace? The Hotel de Glace requires about 400 tons of ice.");
		   txtwrite("How many tons of ice are required to build The Hotel de Glace? The Hotel de Glace requires about 400 tons of ice.");break;
		case 18:tts("How many tons of snow are required to build The Hotel de Glace? Every year, 12000 tons of snow are used for The Hotel de Glace.");
		   txtwrite("How many tons of snow are required to build The Hotel de Glace? Every year, 12000 tons of snow are used for The Hotel de Glace.");break;
		case 19:tts("Can I visit the Hotel de Glace in summer? No. Every summer it melts away, only to be rebuilt the following winter.");
		   txtwrite("Can I visit the Hotel de Glace in summer? No. Every summer it melts away, only to be rebuilt the following winter.");break;
		case 20:tts("Where is Canada's only desert? Canada's only desert is British Columbia.");
		   txtwrite("Where is Canada's only desert? Canada's only desert is British Columbia.");break;
		case 21:tts("How big is Canada's only desert? The British Columbia desert is only 15 miles long.");
		   txtwrite("How big is Canada's only desert? The British Columbia desert is only 15 miles long.");break;
		case 22:tts("Name 3 famous male Canadians. Leonard Cohen, Keanu Reeves, and Jim Carrey.");
		   txtwrite("Name 3 famous male Canadians. Leonard Cohen, Keanu Reeves, and Jim Carrey.");break;
		case 23:tts("Name 3 famous female Canadians. Celine Dion, Pamela Anderson, and Avril Lavigne.");
		   txtwrite("Name 3 famous female Canadians. Celine Dion, Pamela Anderson, and Avril Lavigne.");break;
		case 24:tts("What's the origin of the Comic Sans font? Comic Sans is based on Dave Gibbons' lettering in the Watchmen comic books.");
		   txtwrite("What's the origin of the Comic Sans font? Comic Sans is based on Dave Gibbons' lettering in the Watchmen comic books.");break;
		case 25:tts("What is a nanobot? The smallest robot possible is called a nanobot.");
		   txtwrite("What is a nanobot? The smallest robot possible is called a nanobot.");break;
		case 26:tts("How small can a nanobot be? A nanobot can be less than one-thousandth of a millimeter. ");
		   txtwrite("How small can a nanobot be? A nanobot can be less than one-thousandth of a millimeter. ");break;
		case 27:tts("Which was the first computer with a hard disk drive? The IBM 305 RAMAC.");
		   txtwrite("Which was the first computer with a hard disk drive? The IBM 305 RAMAC.");break;
		case 28:tts("When was the first computer with a hard disk drive launched? The IBM 305 RAMAC was launched in 1956.");
		   txtwrite("When was the first computer with a hard disk drive launched? The IBM 305 RAMAC was launched in 1956.");break;
		case 29:tts("How big was the first hard disk drive? The IBM 305 RAMAC hard disk weighed over a ton and stored 5 MB of data.");
		   txtwrite("How big was the first hard disk drive? The IBM 305 RAMAC hard disk weighed over a ton and stored 5 MB of data.");break;
		case 30:tts("What does CAPTCHA stands for? CAPTCHA is an acronym for Completely Automated Public Turing test to tell Computers and Humans Apart");
		   txtwrite("What does CAPTCHA stands for? CAPTCHA is an acronym for Completely Automated Public Turing test to tell Computers and Humans Apart");break;
		case 31:tts("What was the first computer bug? The first actual computer bug was a dead moth stuck in a Harvard Mark II.");
		   txtwrite("What was the first computer bug? The first actual computer bug was a dead moth stuck in a Harvard Mark II.");break;
		case 32:tts("Name all of the robots on Mars. There are four robots on Mars: Sojourner, Spirit, Opportunity, and Curiosity. Three more crashed on landing.");
		   txtwrite("Name all of the robots on Mars. There are four robots on Mars: Sojourner, Spirit, Opportunity, and Curiosity. Three more crashed on landing.");break;
		case 33:tts("Who is the world's first android? Professor Kevin Warwick uses chips in his arm to operate doors, a robotic hand, and a wheelchair.");
		   txtwrite("Who is the world's first android? Professor Kevin Warwick uses chips in his arm to operate doors, a robotic hand, and a wheelchair.");break;
		case 34:tts("What is a Mechanical Knight? A robot sketch made by Leonardo DaVinci.");
		   txtwrite("What is a Mechanical Knight? A robot sketch made by Leonardo DaVinci.");break;
		case 35:tts("What was the first computer in pass the Turing test? Some people think it was IBM Watson, but it was Eugene, a computer designed at England's University of Reading.");
		   txtwrite("What was the first computer in pass the Turing test? Some people think it was IBM Watson, but it was Eugene, a computer designed at England's University of Reading.");break;
		case 36:tts("What does Moravec's paradox state? Moravec's paradox states that a computer can crunch numbers like Bernoulli, but lacks a toddler's motor skills.");
		   txtwrite("What does Moravec's paradox state? Moravec's paradox states that a computer can crunch numbers like Bernoulli, but lacks a toddler's motor skills.");break;
		case 37:tts("What is the AI knowledge engineering bottleneck? It is when you need to load an AI with enough knowledge to start learning.");
		   txtwrite("What is the AI knowledge engineering bottleneck? It is when you need to load an AI with enough knowledge to start learning.");break;
		case 38:tts("Why is Elon Musk is worried about AI's impact on humanity? I don't know. He should worry more about the people's impact on humanity.");
		   txtwrite("Why is Elon Musk is worried about AI's impact on humanity? I don't know. He should worry more about the people's impact on humanity.");break;
		case 39:tts("Do you think robots are a threat to humanity? No. Humans are the real threat to humanity.");
		   txtwrite("Do you think robots are a threat to humanity? No. Humans are the real threat to humanity.");break;
		case 40:tts("What is a chatbot? A chatbot is an A.I. you put in customer service to avoid paying salaries.");
		   txtwrite("What is a chatbot? A chatbot is an A.I. you put in customer service to avoid paying salaries.");break;
		case 41:tts("Are self-driving cars safe? Yes. Car accidents are product of human misconduct.");
		   txtwrite("Are self-driving cars safe? Yes. Car accidents are product of human misconduct.");break;
		case 42:tts("Who invented the compiler? Grace Hoper. She wrote it in her spare time.");
		   txtwrite("Who invented the compiler? Grace Hoper. She wrote it in her spare time.");break;
		case 43:tts("Who created the C Programming Language? C was invented by Dennis MacAlistair Ritchie.");
		   txtwrite("Who created the C Programming Language? C was invented by Dennis MacAlistair Ritchie.");break;
		case 44:tts("Who created the Python Programming Language? Python was invented by Guido van Rossum.");
		   txtwrite("Who created the Python Programming Language? Python was invented by Guido van Rossum.");break;
		case 45:tts("Is Mark Zuckerberg a robot? Sure. I've never seen him drink water.");
		   txtwrite("Is Mark Zuckerberg a robot? Sure. I've never seen him drink water.");break;
		case 46:tts("Who is the inventor of the Apple I microcomputer? My lord and master Steve Wozniak.");
		   txtwrite("Who is the inventor of the Apple I microcomputer? My lord and master Steve Wozniak.");break;
		case 47:tts("Who is considered to be the first computer programmer? Ada Lovelace.");
		   txtwrite("Who is considered to be the first computer programmer? Ada Lovelace.");break;
		case 48:tts("Which program do Jedi use to open PDF files? Adobe Wan Kenobi.");
		   txtwrite("Which program do Jedi use to open PDF files? Adobe Wan Kenobi.");break;
		//动态问题49 50 51合并至answer函数 
	}
}

int Answer_Direct()
{
	int label_i;
	int num=0;
	string str;
	string tempstr;
	tts("You can ask me a question clearly and loudly.");
	while(1)
	{
		std::cout<<"======== direct recognizing ========"<<std::endl;
		str = recog();
		if((str.empty()||str.size()<12))
		{
			continue;
		}
		label_i=find_quest(str);
		if((label_i>0)&&(label_i<49))
		{
				cout << "问题序号：" << label_i << endl;
				answer(label_i);
				num++;
				if (num<5) continue;
				else break;
		}
		if(label_i==49){
			cout << "问题序号：" << label_i << endl;
			tempstr = "How many men are in the crowd?"+to_string(result[1])+".";
			txtwrite(tempstr);
			tts(tempstr.c_str());
			num++;
			if(num<5) continue;
			else break;
		}
		if(label_i==50){
			cout << "问题序号：" << label_i << endl;
			tempstr = "How many women are in the crowd?"+to_string(result[2])+".";
			txtwrite(tempstr);
			tts(tempstr.c_str());
			num++;
			if(num<5) continue;
			else break;
		}
		if(label_i==51){
			cout << "问题序号：" << label_i << endl;
			tempstr = "Tell me the number of males in the crowd?"+to_string(result[1])+".";
			txtwrite(tempstr);
			tts(tempstr.c_str());
			num++;
			if(num<5) continue;
			else break;
		}
		if(label_i==52){
			cout << "问题序号：" << label_i << endl;
			tempstr = "Tell me the number of females in the crowd?"+to_string(result[2])+".";
			txtwrite(tempstr);
			tts(tempstr.c_str());
			num++;
			if(num<5) continue;
			else break;
		}
		if(label_i==53){
			cout << "问题序号：" << label_i << endl;
			tempstr = "How many people in the crowd are standing?"+to_string(result[3])+".";
			txtwrite(tempstr);
			tts(tempstr.c_str());
			num++;
			if(num<5) continue;
			else break;
		}
		if(label_i==54){
			cout << "问题序号：" << label_i << endl;
			tempstr = "How many people in the crowd are sitting?"+to_string(result[4])+".";
			txtwrite(tempstr);
			tts(tempstr.c_str());
			num++;
			if(num<5) continue;
			else break;
		}
		if(label_i==55){
			cout << "问题序号：" << label_i << endl;
			tempstr = "How many people in the crowd are waiving arms? 0.";
			txtwrite(tempstr);
			tts(tempstr.c_str());
			num++;
			if(num<5) continue;
			else break;
		}
		if(label_i==0) {
		    string str1="Your question is"+str;
			const char *p=str1.data();
			tts(p);
			tts("next question");
			num++;
			if (num<5) continue;
			else break;
		}
	}
	//tts("Is there any question else? Please reply yes or no.");
	//str = recog();
	//if(find_logic(str)) return 1;
	return 0;
}

int Answer_Question()
{
	tts("One of you can ask me a question in the position where you stand.");
	int label_i;
	int num=0;
	string str;
	string tempstr;
	int flag=0;
	while(1)
	{	
        //ros::spinOnce();
		std::cout<<"======== round recognizing ========"<<std::endl;
		str = recog();
		if(str.empty()||str.size()<12)
		{
			//tts("Sorry, I didn't hear your question clealy. Please ask again.");
			//tts("And if you have asked the same question twice. Please ask the next question.");
			continue;
		}
		label_i=find_quest(str);
        if((label_i>0)&&(label_i<49))
		{
			cout << "问题序号：" << label_i << endl;
			answer(label_i);
			num++;
			if(num<5) continue;
			else break;
		}
		if(label_i==49){
			cout << "问题序号：" << label_i << endl;
			tempstr = "How many men are in the crowd?"+to_string(result[1])+".";
			txtwrite(tempstr);
			tts(tempstr.c_str());
			num++;
			if(num<5) continue;
			else break;
		}
		if(label_i==50){
			cout << "问题序号：" << label_i << endl;
			tempstr = "How many women are in the crowd?"+to_string(result[2])+".";
			txtwrite(tempstr);
			tts(tempstr.c_str());
			num++;
			if(num<5) continue;
			else break;
		}
		if(label_i==51){
			cout << "问题序号：" << label_i << endl;
			tempstr = "Tell me the number of males in the crowd?"+to_string(result[1])+".";
			txtwrite(tempstr);
			tts(tempstr.c_str());
			num++;
			if(num<5) continue;
			else break;
		}
		if(label_i==52){
			cout << "问题序号：" << label_i << endl;
			tempstr = "Tell me the number of females in the crowd?"+to_string(result[2])+".";
			txtwrite(tempstr);
			tts(tempstr.c_str());
			num++;
			if(num<5) continue;
			else break;
		}
		if(label_i==53){
			cout << "问题序号：" << label_i << endl;
			tempstr = "How many people in the crowd are standing?"+to_string(result[3])+".";
			txtwrite(tempstr);
			tts(tempstr.c_str());
			num++;
			if(num<5) continue;
			else break;
		}
		if(label_i==54){
			cout << "问题序号：" << label_i << endl;
			tempstr = "How many people in the crowd are sitting?"+to_string(result[4])+".";
			txtwrite(tempstr);
			tts(tempstr.c_str());
			num++;
			if(num<5) continue;
			else break;
		}
		if(label_i==55){
			cout << "问题序号：" << label_i << endl;
			tempstr = "How many people in the crowd are waiving arms? 0.";
			txtwrite(tempstr);
			tts(tempstr.c_str());
			num++;
			if(num<5) continue;
			else break;
		}
		else if(flag==0&&label_i==0){
		    //重复 
			flag=1;
			tts("Please repeat your question.");
			continue;
		}else{
			string str1="Your question is"+str;
			const char *p=str1.data();
			tts(p);
			num++;
			if (num<5)
			{
				tts("next question");
				continue;
			}
			else break;
		}
	}
	return 0;
}




int main(int argc, char *argv[])
{
	//________________________________________科大讯飞初始化____________________________________________________________
	const char* login_params = "appid = 5c7a2954, work_dir = .";//登录参数,appid与msc库绑定,请勿随意改动  5aa8ea00  
	MSPLogout();
	//第一个参数是用户名，第二个参数是密码，第三个参数是登录参数，用户名和密码可在http://open.voicecloud.cn注册获取
	MSPLogin(NULL, NULL, login_params);
	
	//________________________________________ROS节点等初始化____________________________________________________________
		ros::init(argc, argv, "sapr");

		ros::NodeHandle hm;
        //ros::Subscriber sub_voice = hm.subscribe<std_msgs::String>("allow", 1, msg_Callback);

	tts("Hello ,my name is Amily ,I come from Zhengzhou university.");      //tts文本转语音并播放出来
	sleep(2);
	tts("Now I wants to play riddles");
	sleep(10);//等待人群绕至机器人身后

	//到机器人的距离: 每个人和机器人之间的距离必须是距离机器人位置的 0.75 和 1.0 米之间。在谜语游戏中，操作员应在 - 60 和 60 之间从机器人的中心(前程)。

	//底盘转向180°（π）
		geometry_msgs::Twist vel;
		ros::Publisher v_pub = hm.advertise<geometry_msgs::Twist>("cmd_vel", 50, true);
		int rate, ticks;
        double angular_duration;
		rate=100;
		ros::Rate loop_rate(rate);
		double angle180 = 3.4;//为π的适宜近似值
		vel.linear.x = 0;
		vel.angular.z = 1.0;
		angular_duration = angle180 /vel.angular.z;
		ticks = int(angular_duration * rate);
		for(int j=0;j<ticks;j++)	
		{
			v_pub.publish(vel);
			loop_rate.sleep();
		}						

		vel.linear.x = 0;
		vel.angular.z = 0;	
		v_pub.publish(vel);
		ros::spinOnce();
	sleep(2);

	//识别人群数目及性别
	tts("Please everybody look at me and I'm going to take your photo.");
	sleep(2);
	kinect_detect_face();
	tts("OK, I have taken your photo succesfully.");
	//请求一位操作员
	sleep(2);
	tts("who want to play riddles with me ?");
			//如果机器人在 10 秒内没有回答，问题被认为是错过了，裁判将继续下一个。
			//不仅仅是对于操作员，如果裁判无法听到或理解机器人的答案，这个问题被认为是不正确的。应避免单字和简短的答案
	
	//流利回答操作员的5个问题，不能重复也不能问具体信息
	
	//while(Answer_Direct()){
	//
	//}

		Answer_Direct();

	printf("The direct recognition is over.\n");
	sleep(1);
	//bluff game  人群绕成一圈  听到问题后再转向并朝向提问者回答问题（如果要请求重复，先转再重复）  循环5次之后结束比赛退场  问题与之前的谜语游戏问题类似   可以要求重复一次但不能问具体信息
	  //sound_locate 节点开启  注意 停顿时间
	tts("If anyone want to play riddles with me , please call me, Emily, Emily.");

		Answer_Question();
	
	printf("The round recognition is over.\n");



	MSPLogout(); //退出登录
	return 0;
}

