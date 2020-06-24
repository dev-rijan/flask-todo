import 'modules/js/bootstrap';
import moment from 'moment';
import flatpickr from 'flatpickr';
import bsCustomFileInput from 'bs-custom-file-input'

var pluralize = function (word, count) {
  if (count === 1) { return word; }

  return word + 's';
};

var bulkSelectors = {
  'selectAll': '#select_all',
  'checkedItems': '.checkbox-item',
  'colheader': '.col-header',
  'selectedRow': 'table-warning',
  'updateScope': '#scope',
  'itemCount': '#item-count',
  'bulkActions': '#bulk_actions'
};

$(document).ready(function() {
  var minDate = moment()
      .add(5, 'minutes')
      .format('YYYY-MM-DD HH:mm:ss')

  flatpickr('#todo_at', {
    dateFormat: 'Y-m-d H:i:S',
    enableTime: true,
    minDate: minDate
  })

  //Display file name in file input
  bsCustomFileInput.init()

  // Date formatting with momentjs.
  $('.from-now').each(function (i, e) {
    (function updateTime() {
      var time = moment($(e).data('datetime'));
      $(e).text(time.fromNow());
      $(e).attr('title', time.format('MMMM Do YYYY, h:mm:ss a Z'));
      setTimeout(updateTime, 1000);
    })();
  });

  $('.short-date').each(function (i, e) {
    var time = moment($(e).data('datetime'));
    $(e).text(time.format('MMM Do YYYY'));
    $(e).attr('title', time.format('MMMM Do YYYY, h:mm:ss a Z'));
  });

  // Bulk delete.
  $('body').on('change', bulkSelectors.checkedItems, function () {
    var checkedSelector = bulkSelectors.checkedItems + ':checked';
    var itemCount = $(checkedSelector).length;
    var pluralizeItem = pluralize('item', itemCount);
    var scopeOptionText = itemCount + ' selected ' + pluralizeItem;

    if ($(this).is(':checked')) {
      $(this).closest('tr').addClass(bulkSelectors.selectedRow);

      $(bulkSelectors.colheader).hide();
      $(bulkSelectors.bulkActions).show();
    }
    else {
      $(this).closest('tr').removeClass(bulkSelectors.selectedRow);

      if (itemCount === 0) {
        $(bulkSelectors.bulkActions).hide();
        $(bulkSelectors.colheader).show();
      }
    }

    $(bulkSelectors.updateScope + ' option:first').text(scopeOptionText);
    $(bulkSelectors.itemCount).text(scopeOptionText);
  });

  $('body').on('change', bulkSelectors.selectAll, function () {
    var checkedStatus = this.checked;

    $(bulkSelectors.checkedItems).each(function () {
      $(this).prop('checked', checkedStatus);
      $(this).trigger('change');
    });
  });
});

