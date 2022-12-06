// nav높이+contents높이+footer높이 < viewport높이
//  : footer를 viewport 아래에 fix
// nav높이+contents높이+footer높이 >= viewport높이
//  : footer의 fix 속성을 제거함
let nav_h = document.querySelector('div.nav').clientHeight;
let con_h = document.querySelector('div#content').clientHeight; // <- id select값
let footer_h = document.querySelector('footer').clientHeight;
console.log(nav_h, con_h, footer_h)
console.log(window.innerHeight)
doc_h = nav_h + con_h + footer_h
if(doc_h >= window.innerHeight){
    document.querySelector('footer').classList.remove('fixed-bottom')
}