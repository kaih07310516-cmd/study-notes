const students = [
    {name:'Tom',score:80},
    {name:'Jack',score:55},
    {name:'Alice',score:92}
];

//添加学生
function addStudent(name,score){
    students.push({name,score});
    console.log(students);
}

//查找学生
function findStudent(name){
    const found = students.find(student=> student.name ===name )
    if(found){
        console.log(found);
    }else{
        console.log('Student not found');
    }
}

//修改学生信息

function updateScore(name,newscore){
    const found = students.find(student=> student.name ===name );
    if (found){
        found.score = newscore;
    }else{
        console.log('Student not found')
    }
    console.log(students);
}

//删除学生
function deleteStudent(name){
    const found = students.findIndex(student=> student.name ===name );
    if(found !== -1){
        students.splice(found,1);
    }else{
        console.log('Student not found')
    }
    console.log(students);
}

//输出所有学生
function printStudents(){
    for (const student of students){
        if (student.score >= 60){
            console.log(`${student.name} ${student.score} Pass`);
        }else{
            console.log(`${student.name} ${student.score} Fail`);
        }
    }
}

//计算平均分
function getAverageScore(){
    let sum = 0;
    for (const student of students){
        sum += student.score;
    }
    const average = sum/students.length;
    return(`Average:${average}`);
}

//最高分
function getTopStudent(){
    let topstudent = students[0];
    for(const student of students){
        if (student.score > topstudent.score){
            topstudent = student;
    }
}return `Top student:${topstudent.name} ${topstudent.score}`;

}
//成绩排序
function getsortScore(){
    students.sort(function(a,b){
        if(a.score<b.score)return 1;
        if(a.score>b.score)return -1;
        return 0;
    });
    console.log('排名：',students)
}
//找出所有不及格学生和统计及格学生
function getfailStudents(){
    const failStudents = students.filter(student=>student.score < 60);
    const passStudents = students.length - failStudents.length;
    console.log('及格人数为：',passStudents);
    console.log('不及格学生为：',failStudents);
    return failStudents;
    return passStudents;
}
//找出成绩区间学生
function findscoreRangeStudents(min,max){
    const low = Math.min(min,max);
    const up = Math.max(min,max);
    const scoreRangeStudents = students.filter(student=>low <=student.score && student.score<=up);
    console.log(`成绩在${min}到${max}之间的学生为:`,scoreRangeStudents);
    return scoreRangeStudents;
}

addStudent('Bob',55);
findStudent('Tom');
updateScore("Jack",70)
deleteStudent("Jack");
printStudents();
console.log(getAverageScore());
console.log(getTopStudent());
getsortScore();
getfailStudents();
findscoreRangeStudents(70,100);