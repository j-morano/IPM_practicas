
var thisScript = document.currentScript;

/**
 * Get information from web API
 */
function getData(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url);
    xhr.onload = function() {
        if (xhr.status === 200) {
            callback(null, xhr.responseText);
        } else {
            callback(new Error(xhr.statusText));
        }
    };
    xhr.onerror = function() {
        callback(new Error("Network Error"));
    };
    xhr.send();
}

/**
 * Do something with the data
 */
function showDataInstance(error, data) {
    if (error) {
        console.log(error);
        return;
    }

    // Parse data JSON
    var data = JSON.parse(data);
    var mediaTypeToShow = thisScript.getAttribute('data-mediaType');
    if (data.media_type === mediaTypeToShow && mediaTypeToShow === 'image') {
        // Create image element
        // Append url from data as image to article in document
        var img = document.createElement('img');
        img.src = data.url;
        img.className = 'gallery';
        img.draggable = true;
        img.alt = data.title
        img.ondragstart = "drag(event)";
        document.getElementById('images').appendChild(img);
        console.log(error, data);
    } else if (data.media_type === mediaTypeToShow && mediaTypeToShow === 'video') {
        // Create video element
        var videoInfoDiv = document.createElement('div');
        videoInfoDiv.className = 'videoInfo';
        // Append url from data as video to article in document
        var videoInfo = document.createElement('p');
        videoInfo.innerText = data.description;
        videoInfoDiv.appendChild(videoInfo);
        // Show video url
        var videoUrl = document.createElement('a');
        videoUrl.href = data.url;
        videoUrl.innerText = data.url;
        videoUrl.className = 'simple-link';
        videoInfoDiv.appendChild(videoUrl);
        document.getElementById('videos').appendChild(videoInfoDiv);
        console.log(error, data);
    }
}

/**
 * Build list of past 15 days as string
 */
function buildDateList() {
    var dateList = [];
    var today = new Date();
    var date = new Date(today.getFullYear(), today.getMonth(), today.getDate());
    for (var i = 0; i < 20; i++) {
        dateList.push(date.toISOString().substring(0, 10));
        date.setDate(date.getDate() - 1);
    }
    return dateList;
}

/**
 * Iterate through date list and get images for each date
 */
function getDataForDates(dateList) {
    for (var i = 0; i < dateList.length; i++) {
        getData(
            'https://apodapi.herokuapp.com/api?date=' + dateList[i],
            showDataInstance
        );
    }
}

dateList = buildDateList();
getDataForDates(dateList);

