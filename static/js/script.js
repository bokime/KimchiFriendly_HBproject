$('#request-btn').on('click', (evt) => {
    evt.preventDefault();

    console.log(evt.target)

    const url = $('#url_for_sender_request').val()
        console.log(url)

    const maker_id = $('#maker_id').val()
        console.log(maker_id)
    
    $.get(url, {maker_id:maker_id}, (res) => {
        console.log(res)
    })

    alert('Your request has been sent!')

})



// pagination
// const list_items = $(share_zipcode.html)
// const list_element = document.getElementById('list');
// const pagination_element = document.getElementById('pagination');

// let current_page = 1;
// let rows = 5;

// function DisplayList (items, wrapper, rows_per_page, page) {
// 	wrapper.innerHTML = "";
// 	page--;

// 	let start = rows_per_page * page;
// 	let end = start + rows_per_page;
// 	let paginatedItems = items.slice(start, end);

// 	for (let i = 0; i < paginatedItems.length; i++) {
// 		let item = paginatedItems[i];

// 		let item_element = document.createElement('div');
// 		item_element.classList.add('item');
// 		item_element.innerText = item;
		
// 		wrapper.appendChild(item_element);
// 	}
// }

// function SetupPagination (items, wrapper, rows_per_page) {
// 	wrapper.innerHTML = "";

// 	let page_count = Math.ceil(items.length / rows_per_page);
// 	for (let i = 1; i < page_count + 1; i++) {
// 		let btn = PaginationButton(i, items);
// 		wrapper.appendChild(btn);
// 	}
// }

// function PaginationButton (page, items) {
// 	let button = document.createElement('button');
// 	button.innerText = page;

// 	if (current_page == page) button.classList.add('active');

// 	button.addEventListener('click', function () {
// 		current_page = page;
// 		DisplayList(items, list_element, rows, current_page);

// 		let current_btn = document.querySelector('.pagenumbers button.active');
// 		current_btn.classList.remove('active');

// 		button.classList.add('active');
// 	});

// 	return button;
// }

// DisplayList(list_items, list_element, rows, current_page);
// SetupPagination(list_items, pagination_element, rows);

// $(document).ready(function(){
//     $('#share-detail').after('<div id="nav"></div>');
//     var rowsShown = 4;
//     var rowsTotal = $('#share-detail tbody tr').length;
//     var numPages = rowsTotal/rowsShown;
//     for(i = 0;i < numPages;i++) {
//         var pageNum = i + 1;
//         $('#nav').append('<a href="#" rel="'+i+'">'+pageNum+'</a> ');
//     }
//     $('#share-detail tbody tr').hide();
//     $('#share-detail tbody tr').slice(0, rowsShown).show();
//     $('#nav a:first').addClass('active');
//     $('#nav a').bind('click', function(){

//         $('#nav a').removeClass('active');
//         $(this).addClass('active');
//         var currPage = $(this).attr('rel');
//         var startItem = currPage * rowsShown;
//         var endItem = startItem + rowsShown;
//         $('#share-detail tbody tr').css('opacity','0.0').hide().slice(startItem, endItem).
//                 css('display','table-row').animate({opacity:1}, 300);
//     });
// });
