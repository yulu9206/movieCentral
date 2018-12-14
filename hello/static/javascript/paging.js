function pag(listId, pagId, target){
    $(pagId).empty();
    var rowsShown = 5;
    if (!target) {
      $('li').removeClass('target');
      $('li').addClass('target');
      var rowsTotal = $(listId +' li').length;
    }
    else {
      var rowsTotal = $(listId).find('.target').length;
    }

    var numPages = rowsTotal/rowsShown;
    for(i = 0;i < numPages;i++) {
        var pageNum = i + 1;
        $(pagId).append('<a id="pageNum" href="#" rel="'+i+'"><button type="button" class="btn btn-dark">'+pageNum+'</button></a> ');
    }
    $(listId +' li').hide();
    if (!target) {
        $(listId +' li').slice(0, rowsShown).show();
    }
    else {
        $(listId).find('.target').slice(0, rowsShown).show();
    }

    $(pagId +' a:first').addClass('active');
    $(pagId +' a').bind('click', function(){

        $(pagId +' a').removeClass('active');
        $(this).addClass('active');
        var currPage = $(this).attr('rel');
        var startItem = currPage * rowsShown;
        var endItem = startItem + rowsShown;
        if(!target) {
          $(listId +' li').css('opacity','0.0').hide().slice(startItem, endItem).animate({opacity:1}, 300);
        }
        else {
          $(listId).find('.target').css('opacity','0.0').hide().slice(startItem, endItem).animate({opacity:1}, 300);
        }
    });
}
