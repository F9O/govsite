//<!CDATA[
function g(o){return document.getElementById(o);}
function HoverLi(n){
//�����N����ǩ,�ͽ�i<=N;
for(var i=1;i<=3;i++){g('tb_'+i).className='normaltab';g('tbc_0'+i).className='undis';}g('tbc_0'+n).className='dis';g('tb_'+n).className='hovertab';
}
//���Ҫ���ɵ������ת���뽫<li>�е�onmouseover �ĳ� onclick;
//]]>
