# 【幼盾】个性化图片徽章服务！

![](https://unv-shield.librian.net/api/unv_shield?code=1&repo=RimoChan/Librian)
![](https://unv-shield.librian.net/api/unv_shield?code=1&txt=代码质量:好)
![](https://unv-shield.librian.net/api/unv_shield?code=1&txt=萝莉控:是)

你对方形的徽章感到无聊了吗？想要定制属于自己的开源项目徽章了吗？

快来使用<b>unv-shield</b>吧！

<b>unv-shield</b>提供包含自定义图片的徽章服务，可以让你的项目主页更加个性化！


## 使用方法


```
![](https://unv-shield.librian.net/api/unv_shield?code=1&repo=你的名字/repo的名字)
```

把这行代码加入到你的readme中，就会显示成一个徽章，像是这样——

![](https://unv-shield.librian.net/api/unv_shield?code=1&repo=RimoChan/Librian)


## 自定义

你可以通过向url传递不同的参数来自定义你的徽章: 

- `url`  
    > 样例: `url=https://avatars.githubusercontent.com/u/20064807`  
    > ![](https://unv-shield.librian.net/api/unv_shield?code=1&repo=RimoChan/Librian&url=https://avatars.githubusercontent.com/u/20064807)  
     
    把图片换掉。

- `backcolor`   
    > 样例: `backcolor=0000ff`  
    > ![](https://unv-shield.librian.net/api/unv_shield?code=1&backcolor=0000ff)

    设定背景颜色。  
    默认的背景颜色会随图片改变，是自动生成的。  

- `fontcolor`  
    > 样例: `fontcolor=0000ff`  
    > ![](https://unv-shield.librian.net/api/unv_shield?code=1&fontcolor=0000ff)  

    设定文字颜色。  
    默认的文字颜色取决于背景颜色，通常使用白字，背景颜色的亮度高时使用黑字。  

- `scale`  
    > 样例: `scale=2`  
    > ![](https://unv-shield.librian.net/api/unv_shield?code=1&scale=2)  

    让你的徽章整个等比例变大。

- `txt`  
    > 样例: `txt=你好呀!`  
    > ![](https://unv-shield.librian.net/api/unv_shield?code=1&txt=你好呀!) 
     
    把字换掉。

- `border`  
    > 样例: `border=4`  
    > ![](https://unv-shield.librian.net/api/unv_shield?code=1&border=4)  

    设定边框边距和阴影扩散范围。  
    
- `barlen`  
    > 样例: `barlen=100`  
    > ![](https://unv-shield.librian.net/api/unv_shield?code=1&barlen=100)  

    设定徽章的文字条的长度。  
    默认的长度是由文本决定的。  

- `size`  
    > 样例: `size=50`  
    > ![](https://unv-shield.librian.net/api/unv_shield?code=1&size=50)  
    设定徽章尺寸，但是字号不会变。

- `fontsize`  
    > 样例: `fontsize=30`  
    > ![](https://unv-shield.librian.net/api/unv_shield?code=1&fontsize=30)  
    
    设定字体大小.

- `barradius`  
    > 样例: `fontsize=999`  
    > ![](https://unv-shield.librian.net/api/unv_shield?code=1&barradius=999)  

    设定文本条的援交。  

- `anime`  
    > 样例: `anime=5`  
    > ![](https://unv-shield.librian.net/api/unv_shield?code=1&anime=5)  

    设定文本条弹出的动画时间。

- `shadow`  
    > 样例: `shadow=0.9`  
    > ![](https://unv-shield.librian.net/api/unv_shield?code=1&shadow=0.9)  

    设定背景阴影的浓度。


## 特殊参数

- `repo`  
    将文本替换为对应Github Repo的star数量。

嗯，我先做了这一个，之后再一个一个加吧。

如果你心急如焚，也可以给这个Repo提交PR，让unv-shield支持更多数据源。


## 服务架构

(写不动了剩下的下次再写吧……)

