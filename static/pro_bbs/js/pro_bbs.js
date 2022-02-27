$(document).ready(function (){
    $('.delete').on('click', function (){
        if(confirm("정말로 삭제 하시겠습니까?")){
            document.location.href = $(this).data('uri')
        }
    })
})