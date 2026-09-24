/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    //1.准备一个空数组（栈）,建立括号配对字典
    const stack = [];
    const brackets = {')' : '(',']' : '[','}':'{'};
    //2.遍历字符串，遇到左括号push入栈
    //3遇到右括号时，判断如果站内是空的，直接返回flase，栈内有对应左括号，直接出栈，不对应也返回flse
    for (const char of s){
        if(char in brackets){
            const top = stack.pop();
            if(top !== brackets[char]){
                return false;
            }
        }else{
            stack.push(char);
        }
    }
    //遍历完所有字符，栈内为空返回true
    return stack.length === 0;
};