


// jQuery(document).ready(function(){
//     jQuery(".search-box").addClass("display-none");

//     jQuery(".search-button").click(()=>{
//       jQuery(".search-box").removeClass("display-none");

//       jQuery(".search-box").addClass("display-search");

//     });
//   });

var MainImg=document.getElementById('image');

var small_img=document.getElementsByClassName("smallimg");

small_img[0].onclick=function(){

    MainImg.src=small_img[0].src;

}

small_img[1].onclick=function(){

    MainImg.src=small_img[1].src;

}

small_img[2].onclick=function(){

    MainImg.src=small_img[2].src;}




// accordion js

$(document).ready(function(){

    $("#accordion .card .card-link").click(function(){

        if($(this).find("i.fa").hasClass("fa-minus"))

        {

            $(this).find("i.fa").removeClass("fa-minus");

            $(this).find("i.fa").addClass("fa-plus");

        }

        else if($(this).find("i.fa").hasClass("fa-plus"))

        {

            $(this).find("i.fa").removeClass("fa-plus");

            $(this).find("i.fa").addClass("fa-minus");



        }

        $(this).parents(".card").siblings().find(".card-header .card-link i.fa").removeClass("fa-minus");

        $(this).parents(".card").siblings().find(".card-header .card-link i.fa").addClass("fa-plus");

    })

})



// accordion end







