function my_func() {
let my_date = $('<dataTime>').text()
    $.ajax({
        async: true,
        url: 'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json',
        data: {
            key: '67c59b547b84d9de7658ebb921457f4c',
            targetDt: modified_date},
        method: 'GET',
        timeout: 3000,
        dataType: 'json',
        success: function(result) {
            console.log(result)
            $('tbody').empty()
            // <tr>
            //     <td>순위</td>
            //     <td>
            //         <img src=~~~>
            //     </td>   포스터 이미지
            //     <td>영화 제목</td>
            //     <td>개봉일</td>
            //     <td>누적관람객수</td>
            //     <td>
            //         <input type="button" value="삭제" class="btn btn-primary">
            //     </td> 삭제버튼
            //     <td>상세보기</td>
            // </tr>
            for(let i=0;i<10;i++) {
                let tr = $('<tr></tr>')
                let rankTd = $('<td></td>').text(result['boxOfficeResult']['dailyBoxOfficeList'][i]['rank'])
                let imgTd = $('<td></td>')
                let searchTitle = result['boxOfficeResult']['dailyBoxOfficeList'][i]['movieNm'] + " 포스터"
                let img = $('<img />')
                imgTd.append(img)

                $.ajax({
                    async: true,
                    url: 'https://dapi.kakao.com/v2/search/image',
                    method: 'GET',
                    headers: {
                        Authorization: "KakaoAK " + '1d1912440cd92cf0ce61794b6cb3b7fd'
                    },
                    data: {
                        query: searchTitle
                    },
                    timeout: 4000,
                    dataType: 'json',
                    success: function(result) {
                        let imgUrl = result['documents'][0]['thumbnail_url']
                        img.attr('src', imgUrl)
                    },
                    error: function () {
                        alert('뭔가 이상해요!')
                    }
                })

                let titleTd = $('<td></td>').text(result['boxOfficeResult']['dailyBoxOfficeList'][i]['movieNm'])
                let openTd = $('<td></td>').text(result['boxOfficeResult']['dailyBoxOfficeList'][i]['openDt'])
                let assAudiTd = $('<td></td>').text(result['boxOfficeResult']['dailyBoxOfficeList'][i]['audiAcc'])
                let delTd = $('<td></td>')
                let delBtn = $('<input />').attr('type', 'button').attr('value','삭제')
                // btn-primary는 파란색, btn-warning는 노란색, btn-info는 초록색, btn-danger는 빨간색
                delBtn.addClass('btn btn-danger')
                delBtn.on('click', function() {
                    $(this).parent().parent().remove()
                })
                delTd.append(delBtn)
                tr.append(rankTd)
                tr.append(imgTd)
                tr.append(titleTd)
                tr.append(openTd)
                tr.append(assAudiTd)
                tr.append(delTd)
                $('tbody').append(tr)
            }
        },
        error: function() {
            alert('뭔가 이상해요!')
        }
    });
}